# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
# #auth_token = os.environ['TWILIO_AUTH_TOKEN']

account_sid = 'AC03ff4080627e1574244340a83e1a06cc'
auth_token = '2abd33d0e4a8cc2249e7b62feb2e0ff0'

client = Client(account_sid, auth_token)

def send_sms():
    message = client.messages.create(body='Internet Gas Gauge in AZ report delivered to email.',
                                 from_='+17174936470',
                                 to='+15205962566'
                                 )

    print('Text Message Sent.')
    print(message.sid)