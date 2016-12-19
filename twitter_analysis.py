import tweepy
from textblob import TextBlob

# Register on Twitter Dev and create an application to get the following keys
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	text = tweet.text
	print text
	analysis = TextBlob(text).sentiment
	print analysis
	print "\n\n"
