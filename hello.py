from flask import Flask, render_template, json, request

app = Flask(__name__)


#@app.route('/')
#def hello():
   # return "Awesomeness this is going to be the one."


@app.route('/')
def index():
    """ Just a generic index page to show."""
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
