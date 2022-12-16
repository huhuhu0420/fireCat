from requests import request
from flask import Flask, request, render_template, redirect, url_for
import json
app = Flask(__name__)

@app.route("/",methods=["GET"])
@app.route('/chat', methods=[ 'GET',"POST"])
def chatPage():
    return render_template("chat.html")

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route('/post', methods=[ 'POST'])
def pushInfo():
    print(request.data)
    newMessage=json.loads(request.data)
    print(newMessage["name"])
    with open ('chat.txt', 'a') as file:
        print(newMessage['text'])
        file.writelines(newMessage['text'])
    # with open ('data.json', 'r+') as file:
    #     data=file.read()
    #     data=json.loads(data)
    #     data.append(newMessage)
    #     with open ('data.json', 'w') as Writefile:
    #         Writefile.write(json.dumps(data))

    return "ok"

@app.route('/get', methods=[ 'GET'])
def getInfo():
    data=""
    with open ('data.json', 'r+') as file:
        data=file.read()
    response = app.response_class(
        # response=json.dumps(data),
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response 

if __name__ == '__main__':
    app.run()
