import spotipy.oauth2 as oauth2
import requests
import json


credentials = oauth2.SpotifyClientCredentials(
        client_id="e5dc70c1a984472f888c93032327a9f5",
        client_secret="22c2782e5e7f45c6898dcb8bb34a4ee0")

token = credentials.get_access_token()

url = "https://api.spotify.com/v1/search"

params = {
	"query" : "sunflower",
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
# print sData
track = {}
if "tracks" in sData:
	tracks = sData["tracks"]["items"]
	if len(tracks) != 0:
		data = tracks[0]
# 		img1 = ""
# 		spotifyURL = ""
# 		if len(data["images"]) != 0:
# 			img1 = data["images"][0]
# 		if "spotify" in data["external_urls"]:
# 			spotifyURL = data["external_urls"]["spotify"]
# 		artist = {
# 			"spotifyURL" : spotifyURL,
# 			"spotifyPopularity" : str(data["popularity"]),
# 			"spotifyImage" : img1,
# 		}
	for k,v in zip(data.keys(), data.values()):
		print (k, v)