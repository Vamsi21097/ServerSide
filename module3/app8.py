from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index3.html")

@app.route("/more")
def more():
    return render_template("more1.html")