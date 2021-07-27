from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    names=["jyothi","Manaswitha","vamsi","keshav"]
    return render_template("index1.html",names=names)