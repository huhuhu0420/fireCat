from requests import request
from flask import Flask, request, render_template, redirect, url_for
from tinydb import TinyDB
import json
import logging
import pexpect

ncat = None
text = None
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
db = TinyDB('1.json')  # init db
db.truncate()  # clear db

@app.route("/",methods=["GET", "POST"])
def loginPage ():
    if request.method == 'POST':
        ip = request.form['ip']
        print("post : ip => ", ip)
        global ncat
        if(ncat == None):
            fileName = "1.txt"
            print("ncat")
            ncat = pexpect.spawnu('ncat ' + ip + ' 1234 -o '+ fileName)
            ncat.timeout = 3000   # avoid timeout too quick 
        global text
        if text == None:
            text = pexpect.spawnu('python3 src/txt2json.py ' + fileName +' 1.json')
            text.timeout = 3000
        return render_template("chat.html")

    if request.method == 'GET':
        return render_template("login.html")
    

@app.route('/chat', methods=[ 'GET',"POST"])
def chatPage():
    return render_template("chat.html")

@app.route('/post', methods=[ 'POST'])
def pushInfo():
    print(request.data)
    newMessage=json.loads(request.data)
    print(newMessage["name"])
    global ncat
    if(ncat!=None):
        ncat.sendline(newMessage["text"])

    return "ok"

@app.route('/get', methods=[ 'GET'])
def getInfo():
    data=""
    with open ('1.json', 'r+') as file:
        data=file.read()
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response 

if __name__ == '__main__':
    app.run()
