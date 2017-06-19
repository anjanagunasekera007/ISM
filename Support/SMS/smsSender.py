print("lol")

import pip
# from twilio.rest import TwilioRestClient
from twilio.rest import Client

accountsid = "ACc8008922805bf766b88153991d6e843e"
authToken = "6bc98ac0bcaf19b61806db8aa22840bc"

client = Client(accountsid,authToken)

message = client.api.account.messages.create(
    to="+94719795145",
    from_="+94719795145",
    body="Hello boss..!!!"
)