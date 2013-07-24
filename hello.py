from flask import Flask, render_template, json, request
from flask_oauthlib.client import OAuth
from flask import g, session, request, url_for, flash
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.debug = True
app.secret_key = 'Write Something!'

oauth = OAuth(app)

twitter = oauth.remote_app(
    'twitter',
    consumer_key='  ',
    consumer_secret=' ',
    base_url= ' ',
    request_token_url=' ',
    access_token_url=' ',
    authorize_url=' ',

#@app.route('/')
#def hello():
   # return "Awesomeness this is going to be the one."


@app.route('/')
def index():
    """ Just a generic index page to show."""
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
