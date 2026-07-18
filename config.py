import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    
    DATABASE = os.getenv('DATABASE')
    
    USER_NAME = os.getenv('USER_NAME')
    USER_EMAIL = os.getenv('USER_EMAIL')
    USER_PASSWORD = os.getenv('USER_PASSWORD')


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False