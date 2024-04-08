from abc import ABC

class Config(ABC):
    RECAPTCHA_PUBLIC_KEY = '1314 dhhe 0813 29342'
    

class DevConfig(Config):
    SECRET_KEY = '\xd0\xb2W\x05\x11\xaf_\xc8\xb7\xdd<\x80\x9cj\x9aTv\x9c\xe6\x0b\xea\x02\x1eS'
