class Config:
    SECRET_KEY = "AntonioSQL_1707"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'AntonioSQL_1707'
    MYSQL_DB = 'sirf'

config={
    'development': DevelopmentConfig
}