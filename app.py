from flask import Flask, request, jsonify
from util.utils_aws import AwSClient
from flask import render_template
import json
import matplotlib.pyplot as plt
# import jsonify

app = Flask(__name__)
userClient = AwSClient('output')

@app.route("/")
def home():
    original_data = open("block1.txt").read()

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
    a = [[a[i][j] for j in range(4)] for i in range(50)]
    plt.plot(a)

    plt.show()
    return render_template("table.html", arr=a, r=range(50), c=range(4))


# @app.route('/coords')
# def coords():
#     original_data = open("block.txt").read()

#     dic = json.loads(original_data)
#     # print(type(dic))

#     a = [[0 for i in range(4)] for j in range(50)]
#     features = ['humidity', 'air_pressure', 'temp', 'ph']
#     for i in range(50):
#         for j in range(len(features)):
#             vals = dic[str(i)][features[j]].values()
#             sum = 0
#             for z in vals:
#                 sum += float(z)
#             mean = sum / len(vals)
#             a[i][j] = round(mean, 3)
#     return jsonify(a)

if __name__ == '__main__':
    app.run(debug=True)
