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
    author = "3onyc",
    author_email = "3onyc@x3tech.com",
    license = "MIT",
    url = "http://github.com/3onyc/pyhabit",
    download_url = "https://github.com/3onyc/pyhabit/tarball/master"
)
