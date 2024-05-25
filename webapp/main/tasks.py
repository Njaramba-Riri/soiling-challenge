import smtplib
import logging
from flask import current_app
from flask_mail import Message

from webapp import celery, email
from .models import Reminder

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
logs = logging.getLogger(__name__)


@celery.task()
def log(msg):
    return msg

@celery.task(bind=True,
             ignore_result=True,
             default_retry_delay=300,
             max_retries=5)
def remind(self, pk):
    logs.info("Remind worker %d" % pk)
    reminder = Reminder.query.get(pk)
    msg = Message(body="Text %s" % str(reminder.text), recipients=[reminder.email], subject="Your reminder")
    try:
        email.send(msg)
        logs.info("Email sent to %s" % reminder.email)
        return
    except Exception as e:
        logs.error(e)
        self.retry(exc=e)

def on_reminder_save(mapper, connect, self):
    remind.apply_async(args=(self.id,), eta=self.date)
