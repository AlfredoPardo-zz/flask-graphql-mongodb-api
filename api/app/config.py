import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "Development"
    SECRET_KEY = os.getenv("DEV_SECRET_KEY", "We need guns. Lots of guns.")
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {
        'db': 'fgm_db_dev',
        'username':'fgm',
        'password':'fl4sKGr4phQLM0ngO#',
        'host': 'fgm_db', # fgm_db
        'authentication_source':'admin',
        'port': 27017
    }
   
class TestingConfig(BaseConfig):
    CONFIG_NAME = "Testing"
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Unfortunately, no one can be told what The Matrix is. You'll have to see it for yourself.")
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'fgm_db_test',
        'username':'fgm',
        'password':'fl4sKGr4phQLM0ngO#',
        'host': 'fgm_db',
        'authentication_source':'admin',
        'port': 27017
    }

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
