import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import configparser
import json

with open('/data/options.json') as jf:
    jdata=json.load(jf)

test1=jdata['ip-address']
test2=jdata['port']
test3=jdata['client_name']

clientname = test3
hostname = test1
port = test2
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

topicT ="homeassistant/sensor/addontest/config" 
payloadT ={"unique_id":"addontest",
	"device_class": "temperature",
	"name": "addontest",
	"state_topic": "homeassistant/sensor/addontest/state",
	"unit_of_measurement": "'C",
	"icon":"mdi:lamp",
	"value_template":"{{value_json.temperature}}",
	"device": {
	    "identifiers": ["Identifiers Hagronic"],
	    "name": "Hagronic",
	    "sw_version": "Version 2.01",
	    "model": "PIC32",
	    "manufacturer": "Hagronic"
	  }
	}  


topicTasterRelais="homeassistant/switch/kueche/licht_tisch/config"
payloadTasterRelais={
	"unique_id":"licht_tisch",
	"name":"Licht Tisch",
	"state_topic":"homeassistant/switch/kueche/licht_tisch/state",
	"command_topic":"homeassistant/switch/kueche/licht_tisch/set",
	"payload_on":"ON",
	"payload_off":"OFF",
	"state_on":"ON",
	"state_off":"OFF",
	"optimistic": False,
	"qos":0,
	"ratein": True,
		"device": {
	    "identifiers": ["Identifiers Hagronic"],
	    "name": "Hagronic",
	    "sw_version": "Version 2.01",
	    "model": "PIC32",
	    "manufacturer": "Hagronic"
	  }
}

zahl=0

client.publish(topicT,json.dumps(payloadT))
client.publish(topicTasterRelais,json.dumps(payloadTasterRelais))

while True:

    topic = "SW1_KUECHE"
    data = "hello"+str(zahl)+" | "+str(test1)+" | "+str(test2)
    client.publish(topic, json.dumps(data))
    zahl=zahl+1
    
    topicA = "homeassistant/sensor/addontest/state"
    dataA = {'temperature': zahl}
    client.publish(topicA,json.dumps(dataA))
    
    
    time.sleep(10)
