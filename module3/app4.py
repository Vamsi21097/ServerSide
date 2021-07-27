from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    headline="About"
    return render_template("About1.html", headline=headline)