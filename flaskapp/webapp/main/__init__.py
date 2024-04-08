def create_module(app, *args):
    from .controllers import main_blueprint
    
    app.register_blueprint(main_blueprint)
