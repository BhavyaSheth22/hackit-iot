import paho.mqtt.client as paho
from thread_handler.thread_handler import ThreadHandler
import time
from datetime import datetime
import json
import random
import os
import base64

# imgFiles = []
# for filename in os.listdir('./screenshots'):
#     imgFiles.append(filename)

def connect_client(deviceID):
    id_ = "client"+str(deviceID)
    print(f"inside get id: {id_}")

    client_ = paho.Client(id_)
    client_.connect("127.0.0.1", 1884)

    for i in range(10000):
        if True:
            temp = str(random.uniform(20, 30))[:7]
            humidity = str(random.randint(0, 100))
            air_pressure = str(random.uniform(990, 1005))[:7]
            ph = str(random.uniform(0, 14))[:5]
            msg = {
                'i': deviceID,
                't': datetime.now().timestamp(),
                'temp': temp,
                'humidity': humidity,
                'air_pressure': air_pressure,
                'ph': ph
            }
        # else:
        #     file = random.choice(imgFiles)
        #     img = base64.b64encode(open('./screenshots/' + file, 'rb').read())
        #     img = img.decode('utf-8')
        #     msg = {
        #         'i': deviceID,
        #         't': datetime.now().timestamp(),
        #         'img': img
        #     }

        client_.publish('house', json.dumps(msg))
        print(deviceID, "published message")
        time.sleep(0.5)

    client_.disconnect()


def connect_all_clients(number):
    # print("inside connect all client")

    handle = ThreadHandler()

    for i in range(number):
        handle.spawn_thread(connect_client, (i, ))


if __name__ == "__main__":
    # number = int(input("enter pub: "))

    start_time = time.time()
    connect_all_clients(50)
    duration = time.time() - start_time
    print(f"published {number} in {duration} seconds")
