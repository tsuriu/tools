import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.2'
PACKAGE_NAME = 'tools'
AUTHOR = 'Tulio Amancio (tsuriu)'
AUTHOR_EMAIL = 'tsuriu@tuta.io'
URL = 'https://github.com/tsuriu/tools'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Short implementation from others useful python modules.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'pymysql',
      'requests',
      'easysnmp',
      'paramiko'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
