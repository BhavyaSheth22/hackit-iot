import json

# class gen_json:
#     def __init__(self):
#         super().__init__()
#     def make_block():
block = {}
for deviceID in range(50):
    deviceTree = {}
    with open('data/' + str(deviceID) + '.txt', 'r') as datafile, open('timestamps/' + str(deviceID) + '.txt', 'r') as timefile:
        timestamps = timefile.readlines()
        data = datafile.readlines()
        deviceTree = {time[:-1]:data_item[:-1] for time, data_item in zip(timestamps, data)}
        # print(deviceTree)
        block[deviceID] = deviceTree
# print(block)

with open('block.txt', 'w') as f:
    f.write(json.dumps(block))


