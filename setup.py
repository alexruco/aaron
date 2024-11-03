# setup.py

from setuptools import setup, find_packages

setup(
    name="aaron",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "sqlalchemy"
        # Add any other dependencies here
    ],
    description="A package to crawl websites and extract email addresses.",
    author="Alex Ruco",
    author_email="alex@ruco.pt",
    url="https://github.com/alexruco/aaron",
)