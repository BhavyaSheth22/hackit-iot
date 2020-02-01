import paho.mqtt.client as mqtt
import time

#CloudMQTT
# broker_address = 'hairdresser.cloudmqtt.com'
# mqtt_username = 'iexrwcnw'
# mqtt_password = '85IGF3k0vjc4'
# mqtt_port = 17648

broker_address = '10.0.130.123'
mqtt_port = 1884


def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("Connected OK, rc =", rc)
    else:
        print("Bad connection, rc =", rc)

def on_message(client, userdata, message):
    print('\n\tMessage received')
    
    try:
        decoded_msg = message.payload.decode()
        print('\tpayload =', decoded_msg, '\n')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    
    #Process message here


def on_subscribe(client, userdata, mid, granted_qos):
    print('subscribed')


client = mqtt.Client('qwerty', clean_session=False) # stores subscriptions even on disconnect
client.connected_flag=False
client.on_connect=on_connect
client.on_subscribe=on_subscribe
client.on_message=on_message
# client.username_pw_set(username=mqtt_username, password=mqtt_password)


client.connect(host=broker_address, port=mqtt_port)
# client.loop_start()
""" while not client.connected_flag:
    print('Waiting for conn')
    time.sleep(1) """
print('Waiting in main loop')
client.publish('test', 'conn')
client.subscribe('test')
client.loop_forever()
print('loop ended')
# client.loop_stop()
# client.disconnect()
