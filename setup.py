from setuptools import setup, find_packages

setup(
    name = "pyhabit",
    description = "Library to interact with HabitRPG",
    version = "0.3a",
    install_requires=[
        'distribute',
        'requests'
    ],
    packages = find_packages(),
    author = "Xeross",
    author_email = "contact@xeross.me",
    license = "MIT",
    url = "http://github.com/xeross/pyhabit",
    download_url = "https://github.com/xeross/pyhabit/tarball/master"
)
