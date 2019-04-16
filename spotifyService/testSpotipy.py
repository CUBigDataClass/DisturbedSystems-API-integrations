import requests
import json

url = "https://api.spotify.com/v1/search"

params = {
	"query" : "Post Malone",
	"type" : "artist"
}

headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer BQBp76ck5TB_m3f9_rBDat0H6LtUXlICKS1A4oyUrFXpgnsJb8sNqcphCBPcB10nFnyRjboFsjNH32QUrupBT-g3anm_EqP3nqzhdCLzBmZxChSvOcr78JD6_oktzK4KEWss4g_SLCP16B0Bz1fO2ZV1w74txZdvog",
	"q" : "Post Malone"
}

req = requests.get(url,headers=headers, params = params)

print (req.json())