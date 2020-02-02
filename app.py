from flask import Flask
from util.utils_aws import AwSClient
from flask import render_template
import json

import json
app = Flask(__name__)


@app.route("/")
def home():
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

    return render_template("table.html", arr=a, r=range(50), c=range(4))


if __name__ == '__main__':
    app.run(debug=True)
