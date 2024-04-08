from flask import Flask

def create_app(object):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(object)
    
    from .main import create_module as main_create_module
    from .auth import create_module as auth_create_module
    
    main_create_module(app)
    auth_create_module(app)
    
    return app
    
    
