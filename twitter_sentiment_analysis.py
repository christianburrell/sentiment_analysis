from textblob import TextBlob
import spacy
import asent
import tweepy
import re
from datetime import datetime, timedelta
from api_keys.secret import api_key, secret_api_key, access_token, secret_access_token

auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = secret_api_key)
auth_handler.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth_handler)

'''Editable Queries'''
#add search term and amount of tweets you want to recieve
search_term = 'COVID -filter:retweets -filter:replies' # if you don't want retweets or replies: -filter:retweets -filter:replies
tweet_amount = 100
end = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d") # edit number after days = 

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang = 'en', until = end, tweet_mode = "extended").items(tweet_amount)

tweet_list = ''

nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')
nlp.add_pipe("asent_en_v1")

for tweet in tweets:
    tweet = tweet.full_text
    
    replacements = ['http\S+', '#\S+', '@\S+']
    for replacement in replacements:
        tweet = re.sub(replacement, '', tweet, flags = re.IGNORECASE)

    tweet_list += tweet

    textblob_analysis = TextBlob(tweet_list)
    textblob_polarity = textblob_analysis.polarity

    asent_analysis = nlp(tweet_list)
    asent_polarity = asent_analysis._.polarity

print(f"This is textblob's polarity: {textblob_polarity}")
print(f"This is asent's polarity: {asent_polarity}")
