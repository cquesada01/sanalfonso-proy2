class Config:
    SECRET_KEY = 'clave_secreta2022@'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'san_alfonso'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'cesar_quesada1@usmp.pe'
    MAIL_PASSWORD = 'j:]8)/pW%pgD'


config={
    'development': DevelopmentConfig
}