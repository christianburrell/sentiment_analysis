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


`A Positive Result (>0):`

Article title: "Thousands in Argentina welcome back triumphant World Cup winners, Messi"

Source: NBC

```python
url = 'https://www.nbcnews.com/news/latino/thousands-argentina-welcome-messi-winners-world-cup-rcna62539'
```

```txt
Textblob sentiment: 0.22727272727272724
Asent sentiment: neg=0.0 neu=0.351 pos=0.049 compound=0.2515
```

`A Neutral Result (=0):`

Article title: "How earthquakes are measured"

Source: CNN

```python
url = 'https://www.cnn.com/2022/12/20/weather/how-earthquakes-measured-xpn'
```

```txt
Textblob sentiment: 0.018749999999999996
Asent sentiment: neg=0.0 neu=0.0 pos=0.0 compound=0.0
```

`A Negative Result (<0):`

Article title: "Holiday Shoppers Are Cutting Back. And That’s a Bad Sign For the Economy"

Source: CNN

```python
url = 'https://time.com/6241570/retail-sales-holiday-shopping-economy/'
```

```txt
Textblob sentiment: -0.10571428571428569
Asent sentiment: neg=0.126 neu=0.757 pos=0.117 compound=0.0408
```

## Twitter Sentiment Analysis:
1. Replace API_keys and access tokens into the program with your own
2. You can edit any variable under the "Editble Queries" header to get the search result you want

### Examples:

```python
search_term = 'COVID -filter:retweets -filter:replies'
tweet_amount = 100
end = str(datetime.now() - timedelta(days=7)) #can only produce tweets up to a maximum of 7 days. edit number after 'days = '

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang = 'en', since = start, until=end, tweet_mode = "extended").items(tweet_amount)
```

Currently returns a result of:
```txt
This is textblob's polarity: 0.05335560706654452
This is asent's polarity: neg=0.098 neu=0.57 pos=0.096 compound=-0.003
```
