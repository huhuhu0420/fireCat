from requests import request
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route('/chat', methods=['POST', 'GET'])
def chatPage():
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ", user)
        with open ('testChat.txt', 'a') as file:
            file.writelines(user)
    return render_template('chat.html')

if __name__ == '__main__':
    app.run()
