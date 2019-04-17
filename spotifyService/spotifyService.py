import spotipy.oauth2 as oauth2
import requests

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import json

class Track(Resource):
	def get(self, name):
		credentials = oauth2.SpotifyClientCredentials(
		client_id="",
		client_secret="c2782e5e7f45c6898dcb8bb34a4ee0")

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
		client_secret="e5e7f45c6898dcb8bb34a4ee0")

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
					"spotifyImage" : img1,
				}
		return (artist)



app = Flask(__name__)
api = Api(app)

# Create a URL route in our application for "/"
@app.route('/')
def home():
	"""
	This function just responds to the browser ULR
	localhost:6000/
	:return:		the rendered template 'home.html'
	"""
	return render_template('home.html')


api.add_resource(Artist, "/artist/<string:name>")
api.add_resource(Track, "/track/<string:name>")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5600)
