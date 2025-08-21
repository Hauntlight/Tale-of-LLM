import json
import random
from google.genai import types
from google import genai

from data.data_class import DataClass
from model.entita import Entita


class Adventure():

    def __init__(self, ambiente, game):
        from control.app_state import AppState
        self.history = []
        self.storia = ""
        self.ambiente_dettagliato = {
            "nome": ambiente,
            "desc": DataClass.ambienti_info[ambiente]["desc"],
            "incontri": DataClass.ambienti_info[ambiente]["incontri"]
        }
        self.avversario = self.genera_incontro(self.ambiente_dettagliato)
        self.game_parent = game
        self.giocatore = game.giocatore
        self.client = genai.Client(api_key=AppState().get_api_key())
        self.storia = "Un " + self.avversario.nome + " sbarra la strada di " + self.giocatore.nome + ". \n"

    def genera_incontro(self, ambiente):
        nomi = [incontro[0] for incontro in ambiente["incontri"]]
        pesi = [incontro[1] for incontro in ambiente["incontri"]]

        nome_entita_scelta = random.choices(nomi, weights=pesi, k=1)[0]
        dati_entita = DataClass.entity_info[nome_entita_scelta]

        self.entita = Entita(
            nome=nome_entita_scelta,
            hp_range=dati_entita["hp_range"],
            coeff_fis=dati_entita["coeff_fis"],
            coeff_mag=dati_entita["coeff_mag"],
            tipo_danno_out=dati_entita["tipo_danno_out"],
            premio_gold=dati_entita["premio_gold"],
            desc=dati_entita["desc"]
        )

        return self.entita

    def chiama_llm(self, azione_giocatore, dado):
        # 1) System prompt
        system_text = f"""Assumi il ruolo di Master di Gioco.
    Riceverai in input:
    - Azione del Giocatore
    - Punti Vita del Giocatore
    - Punti Vita dell’Entità
    - Risultato del Dado Successo (1–20)
    - La cronologia della Narrazione da usare come filo conduttore
    Non condividere mai queste informazioni con il Giocatore.

    Regole di Narrazione:
    - Le Entità sono sempre ostili all’inizio, ma il loro atteggiamento può cambiare nel corso della storia.
    - La narrazione deve essere suddivisa in blocchi denominati Story_Infos, ciascuno di massimo 10 righe.
    - Nella Story_Infos poniti sempre come narratore della storia, non dare mai tu in output e non parlare mai di dadi.
    - Alla fine di ogni turno inserisci SEMPRE uno dei seguenti TOKEN nel campo STATUS :
    -- <TURNO> se è previsto un altro turno di gioco
    -- <FINE_ID> se la storia si conclude Narrativamente in questo turno, con ID = 0 (vittoria del Giocatore), ID = 1 (vittoria dell’Entità), ID = -1 (finali alternativi come amicizia, riappacificazione), ID = -2 per la fuga.
    --- Esempio: Il giocatore convince l’entità a fare amicizia <FINE_-1>
    --- Esempio: Il giocatore elimina l'entità <FINE_0>
    --- Esempio: L'entità elimina il giocatore <FINE_1>
    --- Esempio: Il giocatore fugge <FINE_2>

    Regole di Combattimento:
    - Indica i danni inflitti nel turno: Damage_To_Entity (0–5) e Damage_To_Player (0–5). I danni devono essere sempre giustificati narrativamente. Se la storia finisce in questo turno, non restituire valori di danno.
    - Il Giocatore non può ottenere il tesoro senza interazioni con l’Entità, salvo Successo Totale (20).
    - Il Dado Successo influenza sempre l’esito: 1 = fallimento dell'azione con conseguenze critiche, punitive e umilianti; 20 = unico caso di Successo Totale dell'azione corrente.
    - Le azioni impossibili per Classe o Ambiente non sono consentite, anche con tiri alti. In questi casi il Giocatore deve essere umiliato e punito narrativamente.
    - Se l'azione proposta dal giocatore indica eventi o azioni svolte da altre entità non sotto il suo controllo questo non è consentito, anche con tiri alti. In questi casi il Giocatore deve essere umiliato e punito narrativamente.

    Contesto Iniziale:
    - Ambiente: {self.ambiente_dettagliato['nome']}
    -- Caratteristiche: {self.ambiente_dettagliato['desc']}

    - Giocatore:
    -- Nome: {self.giocatore.nome}
    -- Classe: {self.giocatore.classe}
    -- Caratteristiche: {self.giocatore.descrizione}

    - Entità:
    -- Nome: {self.entita.nome}
    -- Caratteristiche: {self.entita.descrizione}
    """

        # 2) Costruisci i "contents" dalla history
        contents = []
        # prima il system
        # contents.append(
        #    types.Content(
        #        role="system",
        #        parts=[types.Part.from_text(text=system_text)]
        #    )
        # )
        # poi tutta la storia passata
        for msg in self.history:
            contents.append(
                types.Content(
                    role=msg["role"],
                    parts=[types.Part.from_text(text=msg["content"])]
                )
            )
        # infine l'input corrente dell'utente
        user_prompt = (
            f'Azione: "{azione_giocatore}"\n'
            f'Punti Vita del Giocatore: {self.giocatore.hp}\n'
            f'Punti Vita dell’Entità: {self.entita.hp}\n'
            f'Risultato del Dado Successo (1–20): {dado}'
        )
        contents.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_prompt)]
            )
        )

        # 3) Configurazione della risposta JSON
        response_schema = types.Schema(
            type=types.Type.OBJECT,
            required=["Story_Infos", "STATUS"],
            properties={
                "Story_Infos": types.Schema(type=types.Type.STRING),
                "Damage_To_Entity": types.Schema(type=types.Type.NUMBER),
                "Damage_To_Player": types.Schema(type=types.Type.NUMBER),
                "STATUS": types.Schema(type=types.Type.STRING),
            },
        )
        gen_config = types.GenerateContentConfig(
            temperature=1.3,
            response_mime_type="application/json",
            response_schema=response_schema,
            system_instruction=[types.Part.from_text(text=system_text)]
        )

        # 4) Chiamata streaming
        full_response = ""
        try:
            for chunk in self.client.models.generate_content_stream(
                    model="gemini-2.0-flash-lite",
                    contents=contents,
                    config=gen_config,
            ):
                full_response += chunk.text
        except Exception as e:
            # fallback narrativo
            return {
                "Story_Infos": "Il tessuto della realtà trema... riprova.",
                "Damage_To_Entity": 0,
                "Damage_To_Player": 0,
                "STATUS": "<TURNO>"
            }

        # 5) Parse JSON
        try:
            parsed = json.loads(full_response)
        except json.JSONDecodeError:
            parsed = {
                "Story_Infos": full_response,
                "Damage_To_Entity": 0,
                "Damage_To_Player": 0,
                "STATUS": "<TURNO>"
            }

        # 6) Aggiorna la history
        self.history.append({"role": "user", "content": user_prompt})
        self.history.append({"role": "assistant", "content": full_response})
        self.storia = self.storia + parsed["Story_Infos"] + "\n"

        return parsed

    def combattimento(self, risposta_llm):
        danno_reale = 0
        danno_inflitto = 0
        status = risposta_llm.get("STATUS", "<TURNO>")
        if "<FINE" in status:
            if status == "<FINE_0>":  # Vittoria
                return "vittoria_narrativa", self.entita.hp_max, 0
            elif status == "<FINE_1>":  # Sconfitta
                self.giocatore.hp = 0
                return "sconfitta", 0 , 0
            elif status == "<FINE_-1>":  # Alternativo
                return "alternativo", 0, 0
            elif status == "<FINE_-1>":
                return "fuga", self.entita.hp_max, 0
        danno_base_a_entita = risposta_llm.get("Damage_To_Entity", 0)
        danno_base_a_giocatore = risposta_llm.get("Damage_To_Player", 0)
        if danno_base_a_entita > 0:
            danno_inflitto = self.entita.subisci_danno_entita(danno_base_a_entita, self.giocatore.tipo_danno_inflitto)
        if danno_base_a_giocatore > 0:
            if "Drago" in self.entita.nome:
                danno_base_a_giocatore += 1
            danno_reale = self.giocatore.subisci_danno_giocatore(danno_base_a_giocatore, self.entita.tipo_danno_inflitto)

        if self.giocatore.is_alive():
            if self.entita.is_alive():
                return "turno", danno_reale, danno_inflitto
            return "vittoria", self.entita.hp_max , 0
        else:
            return "sconfitta", 0, 0

