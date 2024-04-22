from flask_login import LoginManager
from flask_bcrypt import Bcrypt

login = LoginManager()
bcrypt = Bcrypt()


login.login_view = "auth.login"
login.login_message = "Kindly login to access the resource you're looking for."
login.session_protection = "strong"
login.login_message_category = "info"

@login.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(user_id)
    

def create_module(app, **kwargs):
    login.init_app(app)
    bcrypt.init_app(app)
    
    from .controllers import auth_blueprint
    
    app.register_blueprint(auth_blueprint)
