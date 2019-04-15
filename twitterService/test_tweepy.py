import tweepy

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

# Making a search!

# The search term you want to find
query = "Dota2"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.user.screen_name,"Tweeted:",tweet.text)


'''

Printing the tweets from some user

# The Twitter user who we want to get tweets from
name = "thtsme_kev"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.text)
'''



'''

Printing the tweets on my timeline

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)
'''
