# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    """All application configurations"""

    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database configurations
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost:5432/rootslifepro_db'