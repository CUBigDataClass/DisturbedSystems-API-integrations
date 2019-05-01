import pyspark
import nltk

# one time download
#nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

sentences = ["Manjunath is a very good boy", "I think they suck to the core!", "I would throw up if her song comes up"]

for sentence in sentences:
	print(sentence)
	ss = sid.polarity_scores(sentence)
	for k in sorted(ss):
		print('{0}: {1}, \n'.format(k, ss[k]))
