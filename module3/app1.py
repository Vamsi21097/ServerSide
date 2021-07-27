from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, world!"
@app.route('/Jyothi')
def Abhilash():
    return "Hello, Jyothi!"
@app.route('/Jyo')
def Abhi():
    return "Hello, Jyo"