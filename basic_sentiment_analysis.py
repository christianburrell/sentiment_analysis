#BASIC SENTIMENT ANALYSIS PROGRAM USING TEXTBLOB (NL PROCESSOR) AND NEWSPAPER (ARTICLE IMPORTER)
from textblob import TextBlob
from newspaper import Article
import spacy
import asent

#gets article into the program:
url = ''
article = Article(url)
article.download()

#gets HTML out of article
article.parse()

#prepare article for NLP
article.nlp()

#print full article text:
text = article.text
#print(f'This is the full text: {text}')

#print summary of the article (what's actually important for analysis)
summary = article.summary
#print(f"This is the text's summary {summary}")

#passes the string into textblob object
blob = TextBlob(summary)

#creates sentiment value with values closer to -1 being negative and values closer to 1 being positive
blob_sentiment = blob.sentiment.polarity
print(f'Textblob sentiment: {blob_sentiment}')

#SPACY SENTIMENT ANALYSIS W/ ASENT API

#create spacy pipeline
nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

# add the rule-based sentiment model
nlp.add_pipe("asent_en_v1")

doc = nlp(summary)
spacy_sentiment = doc._.polarity
print(f'Asent sentiment: {spacy_sentiment}')