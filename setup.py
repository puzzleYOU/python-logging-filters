from setuptools import find_packages, setup

setup(
    name="python-logging-filters",
    version="0.1.3",
    description="standard python logging filters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="puzzleYOU GmbH",
    author_email="scrum@puzzleyou.de",
    url="https://github.com/puzzleYOU/python-logging-filters/",
    license="MIT",
    platforms=["any"],
    packages=find_packages(),
    install_requires=[],
    zip_safe=True,
)
