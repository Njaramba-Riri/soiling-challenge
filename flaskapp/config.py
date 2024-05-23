import os
from abc import ABC
import datetime

basedir = os.path.abspath(os.path.dirname(__name__))

class Config(ABC):
    RECAPTCHA_PUBLIC_KEY = '1314 dhhe 0813 29342'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    TWILIO_ACCOUNT_SID = 'AC06c28c34225c2c4d46827f7099c463a4'
    TWILIO_AUTH_TOKEN = '030c6bd3c7c11f4c34bd815bee84c0c9'
    TWILIO_SENDER = '+13344228084'
    MODEL_PATH = '/home/riri/Desktop/Soiling/src/models'

class DevConfig(Config):
    SECRET_KEY = '\xd0\xb2W\x05\x11\xaf_\xc8\xb7\xdd<\x80\x9cj\x9aTv\x9c\xe6\x0b\xea\x02\x1eS'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "soiling.db")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CELERYBEAT_SCHEDULE = {
        'log-every-30-seconds': {
            'task': 'webapp.main.tasks.log',
            'schedule': datetime.timedelta(seconds=30),
            'args': ("Message",)
            },
        }
