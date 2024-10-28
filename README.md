# python-logging-filters

Filters for standard python logging, e.g. for suppressing noisy
3rd party framework logging.

`python-logging-filters` can be installed via [PyPI](https://pypi.org/project/python-logging-filters/):

`$ pip install python-logging-filters`

## Current implementations

### DjangoHttp404LogFilter

Suppresses Django's default 'Not Found: ...' logging.
See `python_logging_filters.DjangoHttp404LogFilter`.

**NOTE**: At the moment, this filter does only take the desired effect with
production settings and using a mature WSGI-compliant server (not `./manage.py runserver`).
Using the Django debug server or setting `DEBUG = True` issues a "Not Found"
log warning which cannot be trivially filtered.
