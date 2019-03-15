import tweepy
# from textblob import TextBlob
import json

# Read and write (Access level)

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

# Now it's time to create our API object.

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return

        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        # blob = TextBlob(text)
        # sent = blob.sentiment

        if geo is not None:
             geo = json.dumps(geo)

        if coords is not None:
             coords = json.dumps(coords)

        print (name)
        print (loc, coords, geo)

    def on_error(self, status_code):
        if status_code == 420:
        	print ('Something is wrong!')
        	return False
            #returning False in on_data disconnects the stream


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['avengers'])