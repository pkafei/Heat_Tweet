import tweepy
import json
from pymongo import Connection
from bson import json_util
from tweepy.utils import import_simplejson
import pdb
pdb.set_trace()

json = import_simplejson()
mongocon = Connection()

db = conn.mongocon.tstream
col = db.tweets_tail

consumer_key = 'OwdDOkUp4aI751Xnm7fOg'
consumer_secret = 'dfPYN1ZeKEm36prWGYCVqj5RFkGZgu3WLXXwuIIKmUQ'

access_token_key = '476641614-nF3KLIhIHm9WEATgD0GGcK7z3YEgq0NsSu0sHbd6'
access_token_secret = 'g8bjK5kkSEg6CWJS64Id6tOsTgRp9CrrdOENfXhiM'

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)


class StreamListener(tweepy.StreamListener):
    mongocon = Connection()
    db = mongocon.tstream
    col = db.tweets
    json = import_simplejson()

    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        return False

    def on_data(self, data):
        if data[0].isdigit():
            pass
        else:
            col.insert(json.loads(data))
            print (json.loads(data))

l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=1)
setTerms = ['placebranding', 'socialmarketing']
streamer.filter(track = setTerms)
