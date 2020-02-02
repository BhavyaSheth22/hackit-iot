import json
import os
import shutil

# class gen_json:
#     def __init__(self):
#         super().__init__()
#     def make_block():


def gen_json():
    final = {}
    for deviceID in range(50):
        deviceTree = {}
        try:
            timestamps = open('./data/' + str(deviceID) +
                            '/timestamps.txt', 'r').readlines()
            for filename in os.listdir('./data/' + str(deviceID)):
                if filename != 'timestamps.txt':
                    with open('./data/' + str(deviceID) + '/' + filename) as f:
                        data = f.readlines()
                        deviceTree[filename[:-4]] = {time[:-1]: data_item[:-1]
                                                    for time, data_item in zip(timestamps, data)}
            final[str(deviceID)] = deviceTree
        except Exception as ex:
            template = "centre:An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            # print(message)
        try:
            shutil.rmtree('data/' + str(deviceID))
        except OSError as e:
            # print ("gen_json: Error: %s - %s." % (e.filename, e.strerror))
            print('.')

    with open("block.txt", 'w') as f:
        f.write(json.dumps(final))

# gen_json()