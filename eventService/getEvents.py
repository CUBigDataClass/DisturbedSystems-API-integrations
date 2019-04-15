from predicthq import Client
import reverse_geocoder as rg

  
phq = Client(access_token="")

retJ = []

name = "post malone"

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
print retJ;
# return retJ;