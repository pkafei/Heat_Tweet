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
    consumer_key='OwdDOkUp4aI751Xnm7fOg  ',
    consumer_secret='dfPYN1ZeKEm36prWGYCVqj5RFkGZgu3WLXXwuIIKmUQ',
    base_url= ' ',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

#@app.route('/')
#def hello():
   # return "Awesomeness this is going to be the one."


@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@app.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']


@app.route('/login')
def login():
    callback_url = url_for('oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)


@app.route('/logout')
def logout():
    session.pop('twitter_oauth', None)
    return redirect(url_for('base'))


@app.route('/oauthorized')
@twitter.authorized_handler
def oauthorized(resp):
    if resp is None:
        flash('Authentication Error!')
    else:
        session['twitter_oauth'] = resp
    return redirect(url_for('index'))


@app.route('/')
def index():
    """ Just a generic index page to show."""
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
