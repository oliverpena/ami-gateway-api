import logging
from logging.handlers import TimedRotatingFileHandler

from dependency_injector import containers, providers

from core.config import LoggingConfig
from utils.logging_queue_listener import LoggingQueueListenerHandler


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    logging_config = LoggingConfig
    _file_handler = TimedRotatingFileHandler(filename=logging_config.LOG_FILE,
                                             when=logging_config.LOG_WHEN_ROTATE,  # noqa
                                             backupCount=logging_config.LOG_COUNT)  # noqa
    logging = providers.Resource(
        logging.basicConfig(level=logging_config.LOG_LEVEL,
                            format=logging_config.LOG_FORMAT,
                            handlers=[logging.StreamHandler(),
                                      LoggingQueueListenerHandler(
                                handlers=_file_handler)],
                            datefmt=logging_config.LOG_DATE_FORMAT))
