from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST","get"])
def signup():
  error=None
  success=None
  if request.method=='POST':
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')
    password2=request.form.get('Cpassword')

    if len(name)<6:
      error ="Uname should have atleast of 6 characters"
    elif len(password)<8:
      error ="Password should have atleast of 8 characters"
    elif (password!=password2):
      error="password not matched"
    else:
      name=name.capitalize()
      success= "Hello, "+name+" Account Created Successfully"
  return render_template("signup.html", error=error, msg=success)