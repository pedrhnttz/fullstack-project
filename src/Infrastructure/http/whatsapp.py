import random
import os
from twilio.rest import Client

class WhatsApp:
    def whatsApp():
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HX229f5a04fd0510ce1b071852155d3e75',
        content_variables='{"1":"409173"}',
        to='whatsapp:+5511960539593'
        )

        print(message.sid)
    def criacao_token():
        return f"{random.randint(0, 9999):04d}"