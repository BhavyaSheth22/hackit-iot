import paho.mqtt.client as paho
from thread_handler.thread_handler import ThreadHandler
import time
from datetime import datetime
import json
import random

def connect_client(deviceID):
    id_ = "client"+str(deviceID)
    print(f"inside get id: {id_}")

    client_ = paho.Client(id_)
    client_.connect("127.0.0.1",1884)
    
    for i in range(30):
        message = str(random.uniform(20, 30))[:7]
        msg = {
            'i': deviceID,
            't': datetime.now().isoformat(timespec='seconds'),
            'm': message
        }
        print(client_.publish('house', json.dumps(msg)).is_published())
        time.sleep(0.5)
        
    client_.disconnect()
    
def connect_all_clients(number):
    print("inside connect all client")

    handle = ThreadHandler()

    for i in range(number):
        handle.spawn_thread(connect_client, (i, ))
        

if __name__ == "__main__":
    number = int(input("enter pub: "))

    start_time = time.time()
    connect_all_clients(number)
    duration = time.time() - start_time
    print(f"published {number} in {duration} seconds")
