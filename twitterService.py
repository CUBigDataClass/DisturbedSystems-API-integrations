import stateplane
import tweepy
import csv
from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import json
app = Flask(__name__)
api = Api(app)
class User(Resource):
    def get(self, name):
        sCounts = {"US-AL" : 0, "US-AK" : 0, "US-AZ" : 0, "US-AR" : 0, "US-CA" : 0, "US-CO" :
 0, "US-CT" : 0, "US-DE" : 0, "US-FL" : 0, "US-GA" : 0, "US-HI" : 0, "US-ID" : 0, "US-IL" : 0
, "US-IN" : 0, "US-IA" : 0, "US-KS" : 0, "US-KY" : 0, "US-LA" : 0, "US-ME" : 0, "US-MD" : 0, 
"US-MA" : 0, "US-MI" : 0, "US-MN" : 0, "US-MS" : 0, "US-MO" : 0, "US-MT" : 0, "US-NE" : 0, "U
S-NV" : 0, "US-NH" : 0, "US-NJ" : 0, "US-NM" : 0, "US-NY" : 0, "US-NC" : 0, "US-ND" : 0, "US-
OH" : 0, "US-OK" : 0, "US-OR" : 0, "US-PA" : 0, "US-RI" : 0, "US-SC" : 0, "US-SD" : 0, "US-TN
" : 0, "US-TX" : 0, "US-UT" : 0, "US-VT" : 0, "US-VA" : 0, "US-WA" : 0, "US-WV" : 0, "US-WI" 
: 0, "US-WY" : 0}
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)

        if name == '':
            name = 'eminem'

        count = 0
        for tweet in tweepy.Cursor(api.search,q=name, count=100, lang="en", since="2014-04-03").items(6000):
            if tweet.place is not None:
                if tweet.place.country_code == u'US':
                    count = count + 1
                    #print (tweet.created_at, tweet.coordinates, tweet.place, tweet.user.derived.locations.region)
                    cood = tweet.place.bounding_box.coordinates[0][0]
                    # print (cood)
                    tweetState = 'US-'+stateplane.identify(cood[0], cood[1], fmt='short')[:2]
                    sCounts[tweetState] += 1
            if count > 100:
                break

        # print (sCounts)
        return (sCounts)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


api.add_resource(User, "/user/<string:name>")

if __name__ == '__main__':
    app.run(host='0.0.0.0')