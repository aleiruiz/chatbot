from twilio.rest import Client
import os

client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))


def send_message(to, body):
    """
    Send a WhatsApp message to the user.
    """
    client.messages.create(
        from_=os.getenv('TWILIO_WHATSAPP_NUMBER'),
        body=body,
        to=to
    )


