import logging
from logging.handlers import SMTPHandler
from pathlib import Path


class CustomFormatter(logging.Formatter):
    def __init__(self, colors=None, format_string=None):
        self.colors = colors or {
            "grey": "\x1b[38;20m",
            "blue": "\x1b[34;20m",
            "green": "\x1b[32;20m",
            "yellow": "\x1b[33;20m",
            "red": "\x1b[31;20m",
            "bold_red": "\x1b[31;1m",
            "reset": "\x1b[0m",
        }
        self.format_string = (
            format_string
            or "%(levelname)s : %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
        )
        self.FORMATS = {
            logging.DEBUG: f"{self.colors['blue']}{self.format_string}{self.colors['reset']}",
            logging.INFO: f"{self.colors['green']}{self.format_string}{self.colors['reset']}",
            logging.WARNING: f"{self.colors['yellow']}{self.format_string}{self.colors['reset']}",
            logging.ERROR: f"{self.colors['red']}{self.format_string}{self.colors['reset']}",
            logging.CRITICAL: f"{self.colors['bold_red']}{self.format_string}{self.colors['reset']}",
        }
        super().__init__(self.format_string)

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def create_logger(
    name,
    level=logging.DEBUG,
    stream_level=logging.DEBUG,
    file_path="log.log",
    file_level=logging.WARNING,
    smtp_config=None,
):

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Stream Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    stream_handler.setFormatter(CustomFormatter())
    logger.addHandler(stream_handler)

    # File Handler
    file_handler = logging.FileHandler(Path(file_path))
    file_handler.setLevel(file_level)
    file_handler.setFormatter(
        logging.Formatter(
            "%(levelname)s : %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
        )
    )
    logger.addHandler(file_handler)

    # SMTP Handler
    if smtp_config:
        smtp_handler = SMTPHandler(**smtp_config)
        smtp_handler.setLevel(logging.ERROR)
        smtp_handler.setFormatter(
            logging.Formatter(
                "%(levelname)s : %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
            )
        )
        # logger.addHandler(smtp_handler)

    return logger


# مثال برای پاس دادن پارامترها
if __name__ == "__main__":
    smtp_config = {
        "mailhost": ("smtp.gmail.com", 587),
        "fromaddr": "example@gmail.com",
        "toaddrs": ["example@gmail.com"],
        "subject": "Error from App",
    }

    logger = create_logger(
        name=__name__,
        level=logging.INFO,
        stream_level=logging.INFO,
        file_path="custom_log.log",
        file_level=logging.ERROR,
        smtp_config=smtp_config,
    )

    logger.error("This is an error message")
