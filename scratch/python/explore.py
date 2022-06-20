from twilio.rest import Client
client=Client("","")
#for msg in client.messages.list():
 #   print(msg.body)
#msg=client.messages.create(
 #   to="+916390159999",
  #  from_="+16089099079",
   # body="Hello from Python",
 #)
#print(f"Created a new message:{msg.sid}")

for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()