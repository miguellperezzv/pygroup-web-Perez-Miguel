class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATION =  False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI =  'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    TESTING= True
    