from textblob import TextBlob
import tweepy
import sys
from api_keys.secret import api_key, secret_api_key, access_token, secret_access_token
import pandas as pd

auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = secret_api_key)
auth_handler.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth_handler)

search_term = 'covid -filter:retweets -filter:replies'
tweet_amount = 10

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang = 'en').items(tweet_amount)

polarity = 0

for tweet in tweets:
    tweet = tweet.text
    analysis = TextBlob(tweet)
    polarity += analysis.polarity

print(polarity)