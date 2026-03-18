from twilio.rest import Client
import random
import os

account_sid = os.environ['SID']
auth_token = os.environ['TOKEN']


client = Client(account_sid, auth_token)

messages = [
    "Good morning",
    "Hope you have a nice and amazing day",
    "STAY HARD BITCH",
    "YOU DON'T KNOW ME SON!",
    "EVERYTHING HAPPENS FOR A REASON",
    "STAY OF THE WEEEEEED"
]
body=random.choice(messages)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=body,
  to='whatsapp:+919970362553'
)

print(message.sid)