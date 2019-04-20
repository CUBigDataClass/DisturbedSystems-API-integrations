import spotipy.oauth2 as oauth2
import requests
import json


credentials = oauth2.SpotifyClientCredentials(
        client_id="",
        client_secret="")

token = credentials.get_access_token()

url = "https://api.spotify.com/v1/search"

params = {
	"query" : "adventures of rain dance maggie",
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
			"albumID" : aid,
			"energy":"",
			"liveness":"",
			"tempo":"",
			"speechiness":"",
			"acousticness":"",
			"instrumentalness":"",
			"danceability":"",
			"loudness":"",
			"valence":"",
			"preview_url":""
		}

		if tid:
			url = "https://api.spotify.com/v1/audio-features/"+track["trackID"]
			req = requests.get(url,headers=headers)
			tData = req.json()
			track["energy"] = tData["energy"]
			track["liveness"] = tData["liveness"]
			track["tempo"] = tData["tempo"]
			track["speechiness"] = tData["speechiness"]
			track["acousticness"] = tData["acousticness"]
			track["instrumentalness"] = tData["instrumentalness"]
			track["danceability"] = tData["danceability"]
			track["loudness"] = tData["loudness"]
			track["valence"] = tData["valence"]

			url = "https://api.spotify.com/v1/tracks/"+track["trackID"]
			req = requests.get(url,headers=headers)
			tData = req.json()
			track["preview_url"] = tData["preview_url"]
		print (track)