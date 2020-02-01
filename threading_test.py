import paho.mqtt.client as paho
from thread_handler.thread_handler import ThreadHandler
import time
import random

def connect_client():
    id_ = "client"+str(random.randint(0,10000000))
    print(f"inside get id: {id_}")

    client_ = paho.Client(id_)
    client_.connect("127.0.0.1",1883)
    
    for i in range(3):
        print(client_.publish("house", id_ + ": " + str(i)).is_published())
        time.sleep(0.5)
        
    client_.disconnect()
    
def connect_all_clients(number):
    print("inside connect all client")

    handle = ThreadHandler()

    for _ in range(number):
        handle.spawn_thread(connect_client)
        

if __name__ == "__main__":
    number = int(input("enter pub: "))

    start_time = time.time()
    connect_all_clients(number)
    duration = time.time() - start_time
    print(f"published {number} in {duration} seconds")
