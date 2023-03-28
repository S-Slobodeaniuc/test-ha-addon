import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import configparser
import json

with open('/data/options.json') as jf:
    jdata=json.load(jf)

test1=jdata['ip-address']
test2=jdata['port']

clientname = "PythonTest"
hostname = '192.168.1.196'
port = 1883
timeout = 60

# callback for CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# callback for received messages
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(clientname)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("user", "passwd")
client.connect(hostname, port, timeout)

client.loop_start()

zahl=0

while True:

    topic = "SW1_KUECHE"
    data = "hello"+str(zahl)+test1+test2
    client.publish(topic, json.dumps(data))
    zahl=zahl+1
    time.sleep(10)
