from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("Hello World")

@app.route("/b")
def bye_world():
    return ("BYE BYE World")
