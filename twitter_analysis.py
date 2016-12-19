import tweepy
from textblob import TextBlob

consumer_key = "O3O8mMUH6XRLhZVUgVbgal89c"
consumer_secret = "fH6DFDlh8vEV67kuvEMtanXQFGeH1e3Nb2Xuhcc6Fk27YrqjUD"

access_token = "2893651362-U8dOz2WJagtQyGF6UxvBeS6Rn5OYLqmMfYSXWtx"
access_token_secret = "YD2cCiznFjDoklVBjRlabSgytcMFAixdlvCvbRbyRZd7B"

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