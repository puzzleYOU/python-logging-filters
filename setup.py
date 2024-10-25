from setuptools import find_packages, setup

setup(
    name="python-logging-filters",
    version="0.1.0",
    description=(
        "Simple filters for standard python logging, e.g. for suppressing "
        "noisy 3rd party framework logging."
    ),
    author="puzzleYOU GmbH",
    author_email="scrum@puzzleyou.de",
    url="https://www.puzzleyou.de/",
    license="GPLv3",
    platforms=["any"],
    packages=find_packages(),
    install_requires=[],
    zip_safe=True,
)
