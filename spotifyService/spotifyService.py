import spotipy.oauth2 as oauth2
import requests

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import json

class Artist(Resource):
    def get(self, name):
		credentials = oauth2.SpotifyClientCredentials(
        client_id="",
        client_secret="")

		token = credentials.get_access_token()

		url = "https://api.spotify.com/v1/search"

		params = {
			"query" : "pink floyd",
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
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


api.add_resource(Artist, "/artist/<string:name>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5600)
