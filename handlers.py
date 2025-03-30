import logging
from logging import FileHandler, StreamHandler
from logging.handlers import SMTPHandler
from formatters import DefaultFormatter, StremFormatter


class Handlers:
    def __init__(
        self,
        config,
        formatters=None,
        stream_level=logging.DEBUG,
        file_level=logging.WARNING,
    ):

        self.config = config
        self.formatters = formatters or {
            "tream": StremFormatter(),
            "file": DefaultFormatter(),
            "mtp": DefaultFormatter(),
        }
        self.stream_level = stream_level
        self.file_level = file_level

    def create_stream_handler(self):
        handler = StreamHandler()
        handler.setLevel(self.stream_level)
        handler.setFormatter(self.formatters["stream"])
        return handler

    def create_file_handler(self):
        handler = FileHandler(self.config.log_file_path)
        handler.setLevel(self.file_level)
        handler.setFormatter(self.formatters["file"])
        return handler

    def create_smtp_handler(self):
        handler = SMTPHandler(**self.config.smtp_config)
        handler.setLevel(logging.ERROR)  # سطح لاگ برای SMTP به صورت پیش‌فرض ERROR است
        handler.setFormatter(self.formatters["smtp"])
        return handler
