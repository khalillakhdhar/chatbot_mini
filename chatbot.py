
from flask import Flask
import os
from flask import request
import requests

app = Flask(__name__)

@app.route("/webhook")
def hello():
    return (request.args.get("hub.challenge"))

@app.route("/webhook",methods=["POST"])
def recMsg():
    content=request.get_json()
    if(content["object"]=="page"):
        for entry in content["entry"]:
            messagingEvent=entry["messaging"][0]
            messageFromUser=messagingEvent['message']['text']
            sender=messagingEvent["sender"]["id"]
            print(sender)
            print(messageFromUser)
    data = {

        "recipient":{
        "id":sender
        },
        "message":{
        "text":messageFromUser
        }
        }
    r=requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=token",json=data)
    

         
    
    

    return "",200

host=os.environ.get("IP","0.0.0.0")
port=int(os.environ.get("PORT",8000))
app.run(host=host,port=port)