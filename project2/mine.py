#!/usr/bin/python
import re
import sys
import csv
from matplotlib import pyplot
import numpy
import nltk
from textblob import TextBlob as TB
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from afinn import afinn_dic

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweet_id=[]
tw_text=[]
tw_language=[]
tw_time=[]
tw_sentiment_bl=[]
tw_sentiment_af=[]

with open("fulldataset.csv") as csv_file_in:
    reader = csv.DictReader(csv_file_in)
    for row in reader:
        tweet_id.append(row['tweet_id'])
        tw_text.append(row[' tweet_text'])
        tw_language.append(row[' tweet_language'])
        tw_time.append(row[' tweet_time'])
        tw_sentiment_bl.append(-1)
        tw_sentiment_af.append(0)

cross_search = {        \
    'islam':0,          \
    'muslim':0,         \
    'gay':0,            \
    'homophobic':0,     \
    'homophobe':0,      \
    'misogyn':0,        \
    'fuck':0,           \
    'shit':0,           \
    'asshole':0,        \
    'racism':0,         \
    'racist':0,         \
    'isis':0,           \
    'isil':0,           \
    'president':0,      \
    'protest':0,        \
    'liberal':0,        \
    'conservative':0,   \
    'republican':0,     \
    'democrat':0,       \
    'damn':0,           \
    'hate':0,           \
    'proud':0,          \
    'ashamed':0,        \
    'great':0,          \
    ' wall ':0,         \
    'unite':0,          \
    'unity':0,          \
    ' sad':0,           \
    'happy':0,          \
    'fail':0,           \
    ' kill ':0,         \
    'idiot':0,          \
    'trump':0,          \
    'election':0,       \
    'rigged':0,         \
    'impeach':0,        \
    'obama':0,          \
    'clinton':0,        \
    'DNC':0,            \
    'bernie':0,         \
    'sanders':0,        \
    'disrespect':0,     \
    'foreign policy':0, \
    'Canada':0,         \
    'Mexic':0,          \
    'immigrant':0,      \
    'wikileak':0,       \
    'assassinat':0,     \
    ' tax':0,           \
    ' rich ':0,         \
    ' poor':0,          \
    'nazi':0,           \
    'fascis':0,         \
    'socialis':0,       \
    'sexist':0,         \
    'vote':0,           \
    'popular vote':0,   \
    'riot':0,           \
    'electoral':0,      \
    'MAGA':0,           \
    'climate change':0, \
    'cabinet':0,        \
    'establishment':0,  \
    'deport':0,         \
    'america':0,        \
}

country = {
    'ar':0,             \
    'cs':0,             \
    'cy':0,             \
    'da':0,             \
    'de':0,             \
    'en':0,             \
    'es':0,             \
    'et':0,             \
    'eu':0,             \
    'fa':0,             \
    'fi':0,             \
    'fr':0,             \
    'ha':0,             \
    'hi':0,             \
    'ht':0,             \
    'hu':0,             \
    'in':0,             \
    'it':0,             \
    'ja':0,             \
    'ko':0,             \
    'lt':0,             \
    'nl':0,             \
    'no':0,             \
    'pl':0,             \
    'pt':0,             \
    'ro':0,             \
    'ru':0,             \
    'sv':0,             \
    'te':0,             \
    'th':0,             \
    'tl':0,             \
    'tr':0,             \
    'uk':0,             \
    'und':0,            \
    'vi':0,             \
    'vi':0,             \
    'zh':0,             \
}



for index, text in enumerate(tw_text):
    for key, value in cross_search.items():
        if word_in_text(key, text):
            cross_search[key]+=1
    print("\r", 'Keyword Analysis:', index+1, 'out of ', len(tweet_id), 'completed.', end="")

print("\r")
for index, lang in enumerate(tw_language):
    for key, value in country.items():
        if word_in_text(key, lang):
            country[key]+=1
    print("\r", 'Country Analysis:', index+1, 'out of ', len(tweet_id), 'completed.', end="")

print("\n\nTotal Tweets:", len(tweet_id))

print('\nKeyword count:')
for key, value in cross_search.items():
    print('\t',key, value)

print('\nGroup by country:')
for key, value in country.items():
    print('\t',key, value)

pos_tw = 0
neg_tw = 0
nue_tw = 0

for index, text in enumerate(tw_text):
    blob = TB(text)
    #print(text, blob.sentiment.polarity)
    if (blob.sentiment.polarity > 0):
        pos_tw +=1
    elif (blob.sentiment.polarity < 0):
        neg_tw +=1
    else:
        nue_tw +=1
    tw_sentiment_bl[index] = blob.sentiment.polarity

print('\n\nPositive Tweets (blob api):', pos_tw)
print('Negative Tweets (blob api):', neg_tw)
print('Nuetral Tweets (blob api):', nue_tw)
print('\n')


#todo: track which hashtags are used together? - entities hashtags
#todo: preprocessing stopwords, remove word endings?, take out puntuation
#todo weighting based on retweets?
#indico for sentiment API
#setiment based on location
#percentage retweets, hashtags per tweet (are people using hashtags?)
#retweets over time
#word cloud if there is time
#print(tw_sentiment)

for index, tweet in enumerate(tw_text):
    for key, value in afinn_dic.items():
        if(word_in_text(key, tweet)):
            tw_sentiment_af[index] += value
    print("\r", 'AFINN Sentiment Analysis:', index+1, 'out of', len(tweet_id), 'tweets completed.', end="")


pos_tw = 0
neg_tw = 0
nue_tw = 0
high =  0
low = 0

for sen in tw_sentiment_af:
    if sen > 0:
        if sen > high:
            high = sen
        pos_tw +=1
    elif sen < 0:
        if sen < low:
            low = sen
        neg_tw +=1
    else:
        nue_tw +=1

print('\nHigh:',high)
print('Low:',low)

print('\nPositive Tweets (afinn method):', pos_tw)
print('Negative Tweets (afinn method):', neg_tw)
print('Nuetral Tweets (afinn method):', nue_tw)

with open('results.csv', 'a') as results_file:
    writer = csv.writer(results_file, delimiter= '|')
    writer.writerow(['Index','Tweet Text','AFINN Sentiment','Blob Sentiment'])
    for index, tweet in enumerate(tw_text):
        writer.writerow([index+1, tweet, tw_sentiment_af[index], tw_sentiment_bl[index]])
print('Calculations Complete')
