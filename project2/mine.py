#!/usr/bin/python
import re
import csv
from matplotlib import pyplot
import numpy


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

term_x=[]
term_y=[]
lang_x=[]
lang_y=[]

with open("tweets3.csv") as csv_file_in:
    reader = csv.DictReader(csv_file_in)
    for row in reader:
        tweet_id.append(row['tweet_id'])
        tw_text.append(row[' tweet_text'])
        tw_language.append(row[' tweet_language'])
        tw_time.append(row[' tweet_time'])
        
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
    'Mexic':0,         \
    'immigrant':0,      \
    'wikileak':0,       \
    'assassinat':0,     \
    ' tax':0,           \
    ' rich ':0,         \
    ' poor':0,          \
    'nazi':0,           \
    'fascis':0,         \
    'socialis':0,       \
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



for text in tw_text:
    for key, value in cross_search.items():
        if word_in_text(key, text):
            cross_search[key]+=1
for lang in tw_language:
    for key, value in country.items():
        if word_in_text(key, lang):
            country[key]+=1

print("\nTotal Tweets:", len(tweet_id))

print('\nKeyword count:')
for key, value in cross_search.items():
    term_y.append(value)
    term_x.append(key)
    print('\t',key, value)

print('\nGroup by country:')
for key, value in country.items():
    lang_y.append(value)
    lang_x.append(key)
    print('\t',key, value)



