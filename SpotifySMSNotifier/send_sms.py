
from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACb6589df4c4ddb3e8aebc7ff1b6fcca73'
TWILIO_AUTH_TOKEN = 'f4569a714e0cadf6434e6be6e3b20286'
TWILIO_PHONE_NUMBER = '+13259398786'
YOUR_PHONE_NUMBER = '+12897074490'

def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(body=message,
                           from_=TWILIO_PHONE_NUMBER,
                           to=YOUR_PHONE_NUMBER)

if __name__ == "__main__":
    send_sms("Hello from Twilio!")
