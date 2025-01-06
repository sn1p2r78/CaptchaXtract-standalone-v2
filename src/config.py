# Configuration File

class Config:
    # Admin Options
    DEFAULT_LIB_ON_UNAVAILABLE = 'tesseract'
    LIBRARIES_OPTIONS = ['tesseract', 'pytesseract']

    # API Port and Key Management
    API_PORT = 4000
    API_KEYS_MANAGEMENT = False

    # Logging
    LOGFILE = 'image_to_text.applog'
    OUTPUT = 'api_responses.applog'


config = Config()
