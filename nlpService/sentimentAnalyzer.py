import nltk
from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import json

# one time download
# nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

class Donut(Resource):
    def get(self, name):
        retJ = {
        1: [{
            "sentiment": "positive",
            "value": 50
        }, {
            "sentiment": "negative",
            "value": 30
        }, {
            "sentiment": "neutral",
            "value": 20
        }],
        2: [{
            "sentiment": "positive",
            "value": 35
        }, {
            "sentiment": "negative",
            "value": 35
        }, {
            "sentiment": "neutral",
            "value": 30
        }], 3: [{
            "sentiment": "positive",
            "value": 20
        }, {
            "sentiment": "negative",
            "value": 20
        }, {
            "sentiment": "neutral",
            "value": 60
        }], 4: [{
            "sentiment": "positive",
            "value": 50
        }, {
            "sentiment": "negative",
            "value": 30
        }, {
            "sentiment": "neutral",
            "value": 20
        }], 5: [{
            "sentiment": "positive",
            "value": 55
        }, {
            "sentiment": "negative",
            "value": 30
        }, {
            "sentiment": "neutral",
            "value": 15
        }],
        6: [{
            "sentiment": "positive",
            "value": 40
        }, {
            "sentiment": "negative",
            "value": 30
        }, {
            "sentiment": "neutral",
            "value": 30
        }],
        7: [{
            "sentiment": "positive",
            "value": 15
        }, {
            "sentiment": "negative",
            "value": 50
        }, {
            "sentiment": "neutral",
            "value": 35
        }],
        }
        sentences = ["Manjunath is a very good boy","I think they suck to the core!","I would throw up if her song comes up","This was so bad that I actually liked it","The concert was pretty cold and we had to get drunk to enjoy the time","A decent artist, decent talent","OMG OMG OMG post malone just dropped a new album!"]
        try:
            for i, sentence in enumerate(sentences):
                ss = sid.polarity_scores(sentence)
                retJ[(i%7) + 1][0]["value"] = ss["pos"]
                retJ[(i%7) + 1][1]["value"] = ss["neg"]
                retJ[(i%7) + 1][2]["value"] = ss["neu"]
        except KeyError:
            return retJ, 200
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


api.add_resource(Donut, "/donut/<string:name>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
