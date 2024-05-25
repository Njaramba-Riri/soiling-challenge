import os
from abc import ABC
import datetime

basedir = os.path.abspath(os.path.dirname(__name__))

class Config(ABC):
    RECAPTCHA_PUBLIC_KEY = '1314 dhhe 0813 29342'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_TOKEN')
    TWILIO_SENDER = os.environ.get('TWILIO_NUMBER')

class DevConfig(Config):
    SECRET_KEY = '\xd0\xb2W\x05\x11\xaf_\xc8\xb7\xdd<\x80\x9cj\x9aTv\x9c\xe6\x0b\xea\x02\x1eS'
    CACHE_TYPE = 'simple'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') \
        or 'sqlite:///' + os.path.join(basedir, "soiling.db")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
