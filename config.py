import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    DATABASE_URL= os.getenv('DATABASE_URL')
    
    USER_NAME = os.getenv('USER_NAME')
    USER_EMAIL = os.getenv('USER_EMAIL')
    USER_PASSWORD = os.getenv('USER_PASSWORD')
    USER_ROLE = os.getenv('USER_ROLE')


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False