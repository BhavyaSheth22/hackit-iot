import requests
import time


# def connect(host='http://google.com'):
#     try:
#         urllib.request.urlopen(host)
#         return True
#     except:
#         return False


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


while(1):
    i = connect()
    if i == 0:
        # add one json to queue
        print("not connected")
        # time.sleep(2)

    elif i == 1:
        # add to cloud
        print("connected")

    elif i == -1:
        break

    time.sleep(2)
