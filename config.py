import pathlib


class Config:
    def __init__(self, project_root=None, smtp_config=None, log_file_path=None):

        self.project_root = project_root or pathlib.Path(__file__).parent
        self.smtp_config = smtp_config or {
            "mailhost": ("smtp.gmail.com", 587),
            "fromaddr": "example@gmail.com",
            "toaddrs": ["example@gmail.com"],
            "subject": "Error from App",
        }
        self.log_file_path = log_file_path or self.project_root / "log.log"
