import requests
import time
from gen_json import gen_json
from lzma_code import lzma_compress


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


start_time = time.time()

while(1):
    i = connect()
    if i == 0:
        # add one json to queue
        print("not connected")

    elif i == 1:
        # add to cloud
        print("connected")

    elif i == -1:
        break

    elapsed_time = time.time() - start_time
    if(int(elapsed_time) % 10 == 0):
        print("10 secs gone")
