import json
import matplotlib.pyplot as plt

plt.close('all')
original_data = open("block.txt").read()

dic = json.loads(original_data)
# print(type(dic))

a = [[0 for i in range(4)] for j in range(50)]
features = ['humidity', 'air_pressure', 'temp', 'ph']
for i in range(50):
    for j in range(len(features)):
        vals = dic[str(i)][features[j]].values()
        sum = 0
        for z in vals:
            sum += float(z)
        mean = sum / len(vals)
        a[i][j] = round(mean, 3)

plt.plot(a, label='plot')
# plt.plot('Device', 'Humidity', a[0])
# plt.plot('Device', 'Atmospheric pressure', a[1])
# plt.plot('Device', 'Temp', a[2])
# plt.plot('Device', 'ph', a[3])
plt.show()
