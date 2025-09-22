import random
import os
from twilio.rest import Client

class WhatsApp:
    @staticmethod
    def envia_codigo_whatsapp(code, phone):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HX229f5a04fd0510ce1b071852155d3e75',
        content_variables=f'{{"1":"{code}"}}',
        to=f'whatsapp:+{phone}'
        )

        print(message.sid)

    @staticmethod
    def criacao_token():
        return f"{random.randint(0, 9999):04d}"