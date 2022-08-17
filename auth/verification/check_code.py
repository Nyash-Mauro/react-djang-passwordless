import os 
from twilio.rest import Client
from django.conf import settings

class CheckOTP:
    
    def check_otp(email, secret):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
                           .services(settings.SERVICE_ID)\
                           .verification_checks \
                           .create(to=email, code=secret)

        return verification_check.status
