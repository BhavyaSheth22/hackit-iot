import paho.mqtt.client as mqtt
import json
import os
from thread_handler.thread_handler import ThreadHandler
# import time

# CloudMQTT
# broker_address = 'hairdresser.cloudmqtt.com'
# mqtt_username = 'iexrwcnw'
# mqtt_password = '85IGF3k0vjc4'
# mqtt_port = 17648

# Local broker
broker_address = '127.0.0.1'
mqtt_port = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Connected OK, rc =", rc)
    else:
        print("Bad connection, rc =", rc)


def on_message(client, userdata, message):
    print('\n\tMessage received')

    try:
        msg = message.payload.decode()
        print('\tpayload =', msg, '\n')

        # Process message here
        msgDict = json.loads(msg)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if not os.path.isdir(dir_path + '/data/' + str(msgDict['i'])):
            os.mkdir(dir_path + '/data/' + str(msgDict['i']))
        deviceDir = os.path.dirname(dir_path + '/data/' + str(msgDict['i']))
        for key, value in msgDict.items():
            if key == 't':
                with open(deviceDir + '/' + str(msgDict['i']) + '/timestamps.txt', 'a') as f:
                    f.write(str(value) + '\n')
            elif key != 'i':
                with open(deviceDir + '/' + str(msgDict['i']) + '/' + str(key) + '.txt', 'a') as f:
                    f.write(str(value) + '\n')

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


def on_subscribe(client, userdata, mid, granted_qos):
    print('subscribed')


# stores subscriptions even on disconnect
client = mqtt.Client('sub', clean_session=False)
client.connected_flag = False
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
# client.username_pw_set(username=mqtt_username, password=mqtt_password) $ For cloudmqtt


client.connect(host=broker_address, port=mqtt_port)

print('Waiting in main loop')
# client.publish('test', 'conn')
client.subscribe('house')
client.loop_forever()
print('loop ended')
