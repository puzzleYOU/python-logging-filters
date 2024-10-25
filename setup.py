from textwrap import dedent

from setuptools import find_packages, setup

setup(
    name="python-logging-filters",
    version="0.1.0",
    description="standard python logging filters",
    long_description=dedent(
        """
        Simple filters for standard python logging, e.g. for suppressing
        noisy 3rd party framework logging.

        # DjangoHttp404LogFilter

        Suppresses Django's default 'Not Found: ...' logging.
        See the `python_logging_filters.DjangoHttp404LogFilter`
        and the official Django documentation for more details how
        to use and configure that filter.
        """
    ),
    author="puzzleYOU GmbH",
    author_email="scrum@puzzleyou.de",
    url="https://github.com/puzzleYOU/python-logging-filters/",
    license="GPLv3",
    platforms=["any"],
    packages=find_packages(),
    install_requires=[],
    zip_safe=True,
)
