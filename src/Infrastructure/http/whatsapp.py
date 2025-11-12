import random
import os
from twilio.rest import Client

class WhatsApp:
    @staticmethod
    def envia_codigo_whatsapp(code, phone):
        pass

    @staticmethod
    def criacao_token():
        return f"{random.randint(0, 9999):04d}"