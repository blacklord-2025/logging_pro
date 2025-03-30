import logging
from handlers import Handlers


class Logger:
    def __init__(
        self, config, handlers, logger_name=__name__, logger_level=logging.DEBUG
    ):

        self.config = config
        self.handlers = handlers
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)
        self._setup_handlers()

    def _setup_handlers(self):
        self.logger.addHandler(self.handlers.create_stream_handler())
        self.logger.addHandler(self.handlers.create_file_handler())
        # برای فعال کردن SMTP هندلر، خط زیر را uncomment کنید
        # self.logger.addHandler(self.handlers.create_smtp_handler())

    def get_logger(self):
        return self.logger
