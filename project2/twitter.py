#!/usr/bin/python

# Twitter.py 
#this collects the raw data from twitter in json format

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#keys here

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth)
 


class TweetListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            #print(&quot;Error on_data: %s&quot; % str(e))
            print("\nerror\n")
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, TweetListener())
twitter_stream.filter(track=['#trump'])


#http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#http://pastebin.com/bqj3bZhG
#https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/