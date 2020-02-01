import concurrent.futures
import requests
import threading
import time
import paho.mqtt.client as paho
import random

thread_local = threading.local()

def get_client():
    id_ = "client"+str(random.randint(0,10000000))
    print(f"inside get id: {id_}")
    if not hasattr(thread_local, "client"):
        thread_local.client = paho.Client(id_)
    return thread_local.client, id_

def connect_client(a):
    client_, id__ = get_client()
    client_.connect("127.0.0.1",1883)
    
    for i in range(3):
        print(client_.publish("house", id__ + ": " + str(i)).is_published())

    client_.disconnect()
    
def connect_all_clients(number):
    print("inside connect all client")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(connect_client,[i for i in range(number)])

if __name__ == "__main__":
    number = int(input("enter pub: "))

    start_time = time.time()
    connect_all_clients(number)
    duration = time.time() - start_time
    print(f"published {number} in {duration} seconds")
