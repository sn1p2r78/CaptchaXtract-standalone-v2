# Configuration File

port defound

class Config:
    DEFAULT_CONFIG = {
        "DATABASE_URL": "postgresql://mydatabase",
        "API_KEY": "enter_your_api_key_here",
        "PORT": 4000
    }

    def __init__(self):
        for k, v in self.DEFAULT_CONFIG.items():
            setattr(self, k, v.copy())

    def load_config(self):
        "Returns config assigned to the class."
        return self
}

config = Config()
