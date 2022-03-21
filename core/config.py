import logging
import os


class LoggingConfig:
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s.%(msecs)03d - %(name)-4s - %(levelname)-s' \
        '- %(message)s'
    LOG_DATE_FORMAT = os.environ.get(
        'LOG_DATE_FORMAT', default='%Y-%m-%dT%H:%M:%S')
    LOG_WHEN_ROTATE = os.environ.get('LOG_WHEN_ROTATE', default='midnight')
    LOG_COUNT = int(os.environ.get('LOG_COUNT', default=7))
    LOG_FILE = os.environ.get('LOG_FILE', default='./logs/ami-gateway-api.log')


class Config:
    """Base Configuration Class"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP_NAME = os.environ.get(
        'FLASK_APP_NAME', default='ami-rest-api')

    config = {
        'SECRET': SECRET_KEY,
        'FLASK_APP_NAME': FLASK_APP_NAME
    }


class DevelopmentConfig(Config):
    """Development Configuration Class"""
    DEBUG = True


class ProductionConfig(Config):
    """Development Configuration Class"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing Configration Class"""
    DEBUG = True
    TESTING = True


app_config = {'development': DevelopmentConfig,
              'production': ProductionConfig,
              'testing': TestingConfig}
