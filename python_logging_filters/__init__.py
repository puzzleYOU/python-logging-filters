import logging
import re


class DjangoHttp404LogFilter(logging.Filter):
    """Suppresses Django's default 'Not Found: ...' log messages.

    See the Django docs how to attach filters to logging handlers via
    the LOGGING setting.
    """
    PATTERN = re.compile("^Not Found:")

    def filter(self, record: logging.LogRecord) -> bool:
        return (
            self.PATTERN.fullmatch(record.msg) is not None
            and record.levelno == logging.WARNING
            and record.name.startswith("django")
        )
