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
        return 0
    except KeyboardInterrupt:
        return -1
    except:
        return 0


# start_time = time.time()

queue = []

# dbClient = AwSClient('fsociety_database')

while(1):
    time.sleep(5)
    gen_json()
    lzma_compress()
    jsonStr = open('comp_block.txt', 'rb').read()

    i = connect()
    if i == 0:  
        # add one json to queue
        print("Not Connected")
        queue.append(jsonStr)
        # os.remove('block.txt')
        os.rename('block.txt', 'block1.txt')
        os.remove('comp_block.txt')

    # elif i == 1:
    #     # add to cloud
    #     print("Connected to DB")
    #     # print(jsonStr)
    #     # PUSH
    #     while not len(queue) == 0:
    #         dbClient.update(queue[0])
    #         print('Dequeued file to be uploaded')
    #         queue.pop()
    #     dbClient.update(jsonStr)
    #     print('Pushed file to DB')
    #     # os.remove('block.txt')
    #     os.rename('block.txt', 'block1.txt')
    #     os.remove('comp_block.txt')

#     elif i == -1:
#         break

    print('length of queue =', len(queue))
