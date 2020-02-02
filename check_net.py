import requests
import time
from gen_json import gen_json
from lzma_code import lzma_compress
import shutil
import os
from util.utils_aws import AwSClient


def connect():
    url = 'http://www.google.com/'
    timeout = 2
    try:
        _ = requests.get(url, timeout=timeout)
        return 1
    except KeyboardInterrupt:
        return -1
    except:
        return 0


# start_time = time.time()

queue = []

dbClient = AwSClient('fsociety_database')

while(1):
    # elapsed_time = time.time() - start_time
    # if round(elapsed_time) > 10 and round(elapsed_time) % 10 == 0:
    #     print("10 secs gone")

    time.sleep(30)
    gen_json()
    lzma_compress()
    jsonStr = open('comp_block.txt', 'rb').read()

    i = connect()
    if i == 0:
        # add one json to queue
        print("not connected")
        queue.append(jsonStr)
        # os.remove('block.txt')
        # os.remove('comp_block.txt')

    elif i == 1:
        # add to cloud
        print("connected to db, pushing")
        # print(jsonStr)
        # PUSH
        while not len(queue) == 0:
            # dbClient.update(queue[0])
            print('pushed queue[front]')
            queue.pop()
        # dbClient.update(jsonStr)
        # print('pushed current jsonStr')
        # os.remove('block.txt')
        # os.remove('comp_block.txt')

#     elif i == -1:
#         break

    print('length of queue =', len(queue))
