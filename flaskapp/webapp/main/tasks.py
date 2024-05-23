from webapp import celery
from flask import current_app
from .models import Reminder

@celery.task()
def log(msg):
    return msg

@celery.task()
def multiply(x, y):
    return x * y

@celery.task(bind=True, ignore_result=True, 
             default_retry_delay=300, max_retries=5)
def remind(self, pk):
    reminder = Reminder.query.get(pk)

    msg = MIMEText(reminder.text)
    msg['Subject'] = "Your reminder"
    msg['From'] = current_app.config['SMTP_FROM']
    msg['To'] = reminder.email
    try:
        smtp_server = smtplib.SMTP(current_app.config['SMTP_SERVER'])
        smtp_server.starttls()
        smtp_server.login(current_app.config['SMTP_USER'],
                          current_app.config['SMTP_PASSWORD'])
        smtp_server.sendmail("", [reminder.email], msg.as_string())
        smtp_server.close()
        return
    except Exception as e:
        self.retry(exc=e)

def on_reminder_save(mapper, connect, self):
    remind.apply_async(args=(self.id,), eta=self.date)
