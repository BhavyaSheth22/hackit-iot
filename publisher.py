import paho.mqtt.client as paho

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client = paho.Client("control")                           #create client object
client.on_publish = on_publish                          #assign function to callback
client.connect("127.0.0.1",1883)                                 #establish connection
ret = client.publish("house","on")                   #publish
