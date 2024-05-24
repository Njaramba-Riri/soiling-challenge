from flask import current_app, Flask

from twilio.rest import Client

def nofication(app: Flask, receiver: str, name: str, time, sender: str='+13344228084'):
    with app.app_context():
        client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])
        message = client.messages.create(to=receiver,
                                        body=f'Hello there, kindly remind {name} to take a break and visit the restroom in { time } minutes.',
                                        from_=sender)
    
        return message
