import sys
import time
import base64
import obdCodes

import json
import struct
import paho.mqtt.client as mqtt

import dataStoring
UBI_USER = dataStoring.UBI_USER
UBI_PASS = "none"
UBI_BROKER = "things.ubidots.com"

def on_connectUBI(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

clientUBI = mqtt.Client()
clientUBI.username_pw_set(UBI_USER, password=UBI_PASS)
clientUBI.connect(UBI_BROKER)

obdCodes.connectOBD('OBDII')


while True:
    rpm = obdCodes.getRPM()
    speed = obdCodes.getSpeed()
    data = {"rpm":str(rpm),
           "speed": str(speed)}

    #translate the message to json
    json_msg = json.dumps(data)

    clientUBI.publish("/v1.6/devices/obdII",
            payload=json_msg,
            qos=0,
            retain=False)
