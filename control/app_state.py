class AppState:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self._api = ""
