import spotipy.oauth2 as oauth2
import requests

import stateplane
import tweepy
import csv
from predicthq import Client
import reverse_geocoder as rg

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)
api = Api(app)


class Track(Resource):
	def get(self, name):
		credentials = oauth2.SpotifyClientCredentials(
		client_id="",
		client_secret="")

		token = credentials.get_access_token()

		url = "https://api.spotify.com/v1/search"

		params = {
			"query" : name,
			"type" : "track",
			"limit" : 1
		}

		headers = {
			"Accept" : "application/json",
			"Content-Type": "application/json",
			"Authorization": "Bearer "+token,
		}
		req = requests.get(url,headers=headers, params = params)

		sData = req.json()
		req = requests.get(url,headers=headers, params = params)

		sData = req.json()
		# print sData
		track = {}
		if "tracks" in sData:
			tracks = sData["tracks"]["items"]
			if len(tracks) != 0:
				data = tracks[0]
				tid = data["id"]
				eid = data["external_ids"]
				if "isrc" in eid:
					eid = data["external_ids"]["isrc"]
				else:
					eid = "N/A"
				duration = data["duration_ms"]
				popularity = data["popularity"]
				fullName = data["name"]

				artistList = data["artists"]

				album = data["album"]
				albumName = album["name"]
				albumRelease = album["release_date"]
				aid = album["id"]
				albumArt = ""
				spotifyURL = ""
				if len(album["images"]) != 0:
					albumArt = album["images"][0]["url"]
				if "spotify" in album["external_urls"]:
					spotifyURL = album["external_urls"]["spotify"]


				track = {
					"trackID" : tid,
					"isrc" : eid,
					"duration" : duration,
					"popularity" : popularity,
					"fullName" : fullName,
					"albumImage" : albumArt,
					"albumURL" : spotifyURL,
					"albumID" : aid
				}
		return track

class Artist(Resource):
	def get(self, name):
		credentials = oauth2.SpotifyClientCredentials(
		client_id="",
		client_secret="")

		token = credentials.get_access_token()

		url = "https://api.spotify.com/v1/search"

		params = {
			"query" : name,
			"type" : "artist",
			"limit" : 1
		}

		headers = {
			"Accept" : "application/json",
			"Content-Type": "application/json",
			"Authorization": "Bearer "+token,
		}
		req = requests.get(url,headers=headers, params = params)

		sData = req.json()
		artist = {}
		if "artists" in sData:
			artists = sData["artists"]["items"]
			if len(artists) != 0:
				data = artists[0]
				img1 = ""
				spotifyURL = ""
				if len(data["images"]) != 0:
					img1 = data["images"][0]
				if "spotify" in data["external_urls"]:
					spotifyURL = data["external_urls"]["spotify"]
				artist = {
					"spotifyURL" : spotifyURL,
					"spotifyPopularity" : str(data["popularity"]),
					"spotifyImage" : img1["url"],
				}
		return (artist)


class Event(Resource):
    def get(self, name):
                phq = Client(access_token="")
                retJ = []
                if name == '':
                        name = "eminem"
                for event in phq.events.search(q=name, limit=5, sort='rank', category='concerts'):
                        try:
                                cood = event.location
                                local = (rg.search([cood[1],cood[0]]))[0]['name']
                        except IndexError as e:
                                cood = [0,0]
                                local = 'USA'
                 #    this = stateplane.identify(cood[0], cood[1])
                        resp = {
                                "eTitle" : event.title,
                                "eDate" : event.start.strftime('%Y-%m-%d'),
                                "eCountry" : event.country,
                                "eRank" : event.rank,
                                "eLocation" : local,
                                }
                        #     print (event.scope, event.description, event.start.strftime
                # ('%Y-%m-%d'), event.category, event.country, event.rank, event.location, event.labels, event.title)
                #    print(event.rank, event.category, event.title, event.start.strftime('%Y-%m-%d'))
                        retJ.append(resp)
                return retJ, 200

class User(Resource):
    def get(self, name):
        sCounts = {"US-AL" : 0, "US-AK" : 0, "US-AZ" : 0, "US-AR" : 0, "US-CA" : 0, "US-CO" : 0, "US-CT" : 0, "US-DE" : 0, "US-FL" : 0, "US-GA" : 0, "US-HI" : 0, "US-ID" : 0, "US-IL" : 0, "US-IN" : 0, "US-IA" : 0, "US-KS" : 0, "US-KY" : 0, "US-LA" : 0, "US-ME" : 0, "US-MD" : 0, "US-MA" : 0, "US-MI" : 0, "US-MN" : 0, "US-MS" : 0, "US-MO" : 0, "US-MT" : 0, "US-NE" : 0, "US-NV" : 0, "US-NH" : 0, "US-NJ" : 0, "US-NM" : 0, "US-NY" : 0, "US-NC" : 0, "US-ND" : 0, "US-OH" : 0, "US-OK" : 0, "US-OR" : 0, "US-PA" : 0, "US-RI" : 0, "US-SC" : 0, "US-SD" : 0, "US-TN" : 0, "US-TX" : 0, "US-UT" : 0, "US-VT" : 0, "US-VA" : 0, "US-WA" : 0, "US-WV" : 0, "US-WI" : 0, "US-WY" : 0}
        consumer_key = ""
        consumer_secret = ""
        access_token = "-9GKZ9iNzp44Yklt7ld0DKyrHQSHPZm8Y8SviTe9"
        access_token_secret = ""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)

        if name == '':
            name = 'eminem'

        count = 0
        for tweet in tweepy.Cursor(api.search,q=name, count=100, lang="en", since="2014-04-03").items(2500):
            if tweet.place is not None:
                if tweet.place.country_code == u'US':
                    count = count + 1
                    #print (tweet.created_at, tweet.coordinates, tweet.place, tweet.user.derived.locations.region)
                    cood = tweet.place.bounding_box.coordinates[0][0]
                    print (cood)
                    tweetState = 'US-'+stateplane.identify(cood[0], cood[1], fmt='short')[:2]
                    if tweetState in sCounts.keys():
                        sCounts[tweetState] += 1
            if count > 100:
                break

        retJ = []
        for k,v in zip(sCounts.keys(), sCounts.values()):
            retJ.append({"id": k, "value":v})

        print (sCounts)
        return (retJ)



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
api.add_resource(Event, "/event/<string:name>")
api.add_resource(Track, "/track/<string:name>")
api.add_resource(Artist, "/artist/<string:name>")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
