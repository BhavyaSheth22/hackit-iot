import concurrent.futures
import requests
import threading
import time
import paho.mqtt.client as paho
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

    thread_list = list()

    for _ in range(number):
        t = threading.Thread(target=connect_client)
        thread_list.append(t)
        t.start()

if __name__ == "__main__":
    number = int(input("enter pub: "))

    start_time = time.time()
    connect_all_clients(number)
    duration = time.time() - start_time
    print(f"published {number} in {duration} seconds")
