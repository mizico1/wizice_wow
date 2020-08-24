# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():              
    return render_template('qna.html')

@app.route('/keyboard')
def keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["�����ϱ�"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == "�����ϱ�":
        dataSend ={
            "message" : {
                "text" : "�����ϱ� �׽�Ʈ�Դϴ�."
            }
        }

    elif content == "�����ϱ�":
        dataSend ={
            "message" : {
                "text" : "������ ����, ����, �������θ� �Է����ּ���."
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":              
    app.run(host="167.71.217.249", port="9093")
