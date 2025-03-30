import logging


class DefaultFormatter(logging.Formatter):
    def __init__(self, format_string=None):
        format_string = (
            format_string
            or "%(levelname)s : %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
        )
        super().__init__(format_string)


class StremFormatter(logging.Formatter):
    def __init__(self, format_string=None, colors=None):
        self.reset = "\x1b[0m"
        self.colors = colors or {
            "grey": "\x1b[38;20m",
            "blue": "\x1b[34;20m",
            "green": "\x1b[32;20m",
            "yellow": "\x1b[33;20m",
            "red": "\x1b[31;20m",
            "bold_red": "\x1b[31;1m",
        }

        format_string = (
            format_string
            or "%(levelname)s : %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
        )
        self.FORMATS = {
            logging.DEBUG: f"{self.colors['blue']}{format_string}{self.reset}",
            logging.INFO: f"{self.colors['green']}{format_string}{self.reset}",
            logging.WARNING: f"{self.colors['yellow']}{format_string}{self.reset}",
            logging.ERROR: f"{self.colors['red']}{format_string}{self.reset}",
            logging.CRITICAL: f"{self.colors['bold_red']}{format_string}{self.reset}",
        }
        super().__init__(format_string)

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
