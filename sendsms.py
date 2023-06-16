from twilio.rest import Client

account_sid = 'AC2b08a59703b19f511a10bb22d3bfb7ff'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18339073425',
    body='tested via VS code',
    to='+11234567890'
)

print(message.sid)
