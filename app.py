from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
    #return render_template("index.html")