import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Awesomeness this is going to be the one."

