import logging
import re
import warnings


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
        message = self._format_message(record)
        is_not_found_record = (
            self.PATTERN.match(message) is not None
            and record.levelno == logging.WARNING
            and record.name.startswith("django")
        )
        return not is_not_found_record

    def _format_message(self, record: logging.LogRecord) -> str:
        if not isinstance(record.msg, str):
            warnings.warn(self._format_type_warning(record.msg))

        # NOTE: 'record.msg' is typed as 'str' but casted explicitly as some
        # immature third-party rant passes 'anything' causing the regex pattern
        # matching in .filter() to fail -.-
        try:
            return str(record.msg) % record.args
        except TypeError:
            return str(record.msg)

    def _format_type_warning(self, value: object):
        return (
            "[DjangoHttp404LogFilter] received non-str object. "
            f"trying to cast {value.__class__} into str"
        )
