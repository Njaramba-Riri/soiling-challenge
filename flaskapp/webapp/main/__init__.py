from sqlalchemy import event
from .models import Reminder, db
from .tasks import on_reminder_save

def create_module(app, *args):
    event.listen(Reminder, 'after_insert', on_reminder_save)
    from .controllers import main_blueprint
    app.register_blueprint(main_blueprint)
