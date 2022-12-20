# Sentiment Analysis Programs
A github repository made to dive into NLP's sentiment analysis capabilities.
Two main programs:
1. Basic Sentiment Analysis
2. Twitter Sentiment Analysis

# Getting Started
1. Clone the repo or download the zip to get started.
2. Open terminal and navigate to the project folder
```zsh
cd sentiment_analysis
```
3. Run requirements.txt file
```zsh
pip install -r requirements.txt
```

## Basic Sentiment Analysis:
- Program designed for an input of a wesbite link in which the program will rate the link's text on a scale from -1 to 1. 
- 1 is deemed as a **"positive"** article while -1 is deemed as a **"negative"** article.

### Instructions:
1. Input website into:
```python
url = ''
```
2. Run code and generate an outcome.

### Examples:


`A Positive Result (>.5):`

Article title: ""

Source: CNN

```python
url = ''
```
`A Neutral Result (=0):`

Article title: ""

Source: CNN

```python
url = ''
```

`A Negative Result (< -.5):`

Article title: ""

Source: CNN

```python
url = ''
```

## Twitter Sentiment Analysis:
1. Replace API_keys and access tokens into the program with your own
2. You can edit any variable under the "Editble Queries" header to get the search result you want

### Examples:

```python
search_term = 'COVID -filter:retweets -filter:replies'
tweet_amount = 100
start = '2022-12-19'
end = '2022-12-12'

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang = 'en', since = start, until=end, tweet_mode = "extended").items(tweet_amount)
```

- Will return a result of: