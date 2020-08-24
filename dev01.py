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
        "buttons" : ["시작하기"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == "시작하기":
        dataSend ={
            "message" : {
                "text" : "시작하기 테스트입니다."
            }
        }

    elif content == "질문하기":
        dataSend ={
            "message" : {
                "text" : "질문할 과목, 내용, 공개여부를 입력해주세요."
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":              
    app.run(host="167.71.217.249", port="9093")
