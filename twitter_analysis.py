from textblob import TextBlob
import tweepy
import sys
from api_keys.secret import api_key, secret_api_key, access_token, secret_access_token

auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = secret_api_key)
auth_handler.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth_handler)

search_term = 'stocks'
tweet_amount = 100

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang = 'en').items(tweet_amount)

polarity = 0

for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position + 2]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position + 2]
        analysis = TextBlob(final_text)
        polarity += analysis.polarity

print(polarity)