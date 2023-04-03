class Config(object):
    DEBUG = False
    TESTING = False
    TEMPLATE_AUTO_RELOAD = True


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
