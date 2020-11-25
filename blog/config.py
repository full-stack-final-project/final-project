import os

root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 5555
    MAIL_USE_SSL = True
    MAIL_ADDRESS = os.getenv('MAIL_ADDERSS')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    #MAIL_SENDER = ('Blog Admin', MAIL_ADDERSS)

    ARTICLE_PER_PAGE = 10
    MANAGE_ARTICLE_PER_PAGE = 10
    MANAGE_COMMENT_PER_PAGE = 20

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(root, 'dev.db')

class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI', 'sqlite:////' + os.path.join(root, 'dev.db'))
    
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}