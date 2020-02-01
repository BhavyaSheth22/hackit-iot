import json
import os

# class gen_json:
#     def __init__(self):
#         super().__init__()
#     def make_block():


def gen_json():
    final = {}
    for deviceID in range(50):
        deviceTree = {}
        timestamps = open('data/' + str(deviceID) +
                          '/timestamps.txt', 'r').readlines()
        for filename in os.listdir('./data/' + str(deviceID)):
            if filename != 'timestamps.txt':
                with open('./data/' + str(deviceID) + '/' + filename) as f:
                    data = f.readlines()
                    deviceTree[filename[:-4]] = {time[:-1]: data_item[:-1]
                                                 for time, data_item in zip(timestamps, data)}
        final[str(deviceID)] = deviceTree

    with open("block.txt", 'w') as f:
        f.write(json.dumps(final))
