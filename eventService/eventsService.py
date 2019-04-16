from predicthq import Client
import reverse_geocoder as rg

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import json

class Event(Resource):
    def get(self, name):
		phq = Client(access_token="bKPnk6kxhqUhRiTj10i6Lgni0Ep4c8")

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



app = Flask(__name__)
api = Api(app)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


api.add_resource(Event, "/event/<string:name>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)