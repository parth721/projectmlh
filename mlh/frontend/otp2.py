from django.conf import settings
from twilio.rest import Client
import random

class MessageHandler:
    phone_number =None
    otp = None
    #constructor
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp
        
    #function for sending otp
    def send_otp_on_phone(self):
        client = Client('AC157a3deced6810930de61fcd331c090d', '22a173d4fad92dedf5ba699ca09fea7e')
        
        message = client.messages.create(
            body="Your OTP : {self.otp}",
            from_='+15178360990',
            to=self.phone_number
        )