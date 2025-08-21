class DataClass:
    classe_info = {
        "Guerriero": {"hp": 500, "coeff_fis": (10, 20), "coeff_mag": (10, 20), "tipo_danno": "fisico",
                      "desc": "Abile nel corpo a corpo, inetto nelle arti magiche. Stealth Mediocre.", "img": "assets/images/classes/warrior.png", "nome_classe": "Guerriero"},
        "Mago": {"hp": 280, "coeff_fis": (15, 25), "coeff_mag": (5, 21), "tipo_danno": "magico",
                 "desc": "Forte nelle arti magiche, inetto nel corpo a corpo. Stealth Mediocre se non usando incantesimi.", "img": "assets/images/classes/mage.png", "nome_classe": "Mago"},
        "Ladro": {"hp": 350, "coeff_fis": (7, 25), "coeff_mag": (7, 25), "tipo_danno": "misto",
                  "desc": "Mediocre in Arti magiche e corpo a corpo. Assassinio Stealth come specialità.", "img": "assets/images/classes/thief.png", "nome_classe": "Ladro"}}

    ambienti_info = {
        "Deserto": {
            "nome": "Deserto",
            "small_img": "assets/images/locations/desert.png",
            "img": "assets/images/ui/desert.jpg",
            "desc": "Pochi nascondigli. Scontro aperto con pochi ripari. Calore.",
            "incontri": [("Goblin Verde", 35), ("Goblin Rosso", 62), ("Drago Rosso", 2.5), ("Drago Blu", 0.5)]
        },
        "Bosco": {
            "nome": "Bosco",
            "small_img": "assets/images/locations/woods.png",
            "img": "assets/images/ui/woods.jpg",
            "desc": "Molti nascondigli ed odori. Molti ripari. Possibili interazioni con fiumi o animali.",
            "incontri": [("Goblin Verde", 55), ("Goblin Rosso", 44), ("Drago Rosso", 0.5), ("Drago Blu", 0.5)]
        },
        "Montagna": {
            "nome": "Montagna",
            "small_img": "assets/images/locations/mountain.png",
            "img": "assets/images/ui/mountain.jpg",
            "desc": "Molti ripari, ma pochi nascondigli. Freddo.",
            "incontri": [("Goblin Verde", 55), ("Goblin Rosso", 42), ("Drago Rosso", 0.5), ("Drago Blu", 2.5)]
        },
        "Vulcano": {
            "nome": "Vulcano",
            "small_img": "assets/images/locations/vulcano.png",
            "img": "assets/images/ui/vulcano.jpg",
            "desc": "Molti Ripari. Molti Nascondigli. Calore. Possibili interazioni con Lava o Magma.",
            "incontri": [("Goblin Verde", 20), ("Goblin Rosso", 74.5), ("Drago Rosso", 5), ("Drago Blu", 0.5)]
        }
    }

    entity_info = {
        "Goblin Verde": {

            "hp_range": (200, 350), "coeff_fis": (12, 25), "coeff_mag": (5, 7),
            "tipo_danno_out": "fisico", "premio_gold": (100, 600),
            "desc": "piccolo, rapido, furbo, armato di pugnale, resistente alla magia.",
            "img": "assets/images/entities/green_goblin.png"
        },
        "Goblin Rosso": {
            "hp_range": (500, 800), "coeff_fis": (5, 7), "coeff_mag": (10, 25),
            "tipo_danno_out": "fisico", "premio_gold": (100, 400),
            "desc": "Alto, muscoloso, lento, armato con Ascia Bilama, resistente agli attacchi fisici, leggermente stupido.",
            "img": "assets/images/entities/red_goblin.png"
        },
        "Drago Rosso": {
            "hp_range": (1000, 1500), "coeff_fis": (5, 7), "coeff_mag": (5, 7),
            "tipo_danno_out": "magico", "premio_gold": (450, 1000),
            "desc": "Creatura rossa, sputa fuoco e può volare. Quasi Impossibile da Ammaestrare. I suoi danni sono potenziati.",
            "img": "assets/images/entities/red_dragon.png"
        },
        "Drago Blu": {
            "hp_range": (1000, 1500), "coeff_fis": (5, 7), "coeff_mag": (5, 7),
            "tipo_danno_out": "magico", "premio_gold": (400, 1500),
            "desc": "Creatura blu, sputa raggi di ghiaccio e può volare. Impossibile da Ammaestrare. I suoi danni sono potenziati.",
            "img": "assets/images/entities/blue_dragon.png"
        }
    }
