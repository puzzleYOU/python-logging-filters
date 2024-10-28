import logging
import re


class DjangoHttp404LogFilter(logging.Filter):
    """Suppresses Django's default 'Not Found: ...' log messages.

    This filter can be integrated into the django `LOGGING` setting,
    see the following excerpt as an example:

    LOGGING = {
        ...,
        "handlers": {
            "console": {
                ...,
                "filters": ["http404"],
            },
        },
        "filters": {
            "http404": {
                "()": "python_logging_filters.DjangoHttp404LogFilter",
            }
        },
        ...,
    }

    NOTE: At the moment, this filter does only take the desired effect with
    production settings and using a mature WSGI-compliant server (not
    `./manage.py runserver`). Using the Django debug server or setting
    `DEBUG = True` issues a "Not Found" log warning which cannot be trivially
    filtered.
    """
    PATTERN = re.compile("^Not Found:")

    def filter(self, record: logging.LogRecord) -> bool:
        return (
            self.PATTERN.fullmatch(record.msg) is not None
            and record.levelno == logging.WARNING
            and record.name.startswith("django")
        )
