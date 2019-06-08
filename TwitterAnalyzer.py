import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
from tokens import *

class listener(StreamListener):
    
    def on_data(self, data):
        
        #Loading all the data
        allData = json.loads(data)
        
        tweet = allData["text"]
        
        #Takes the data from twitter and returns classification and confidence
        sentimenValue, confidenceLevel = s.sentiment(tweet)
        
        #Printing live tweets including their sentiment value and confidence level
        print(tweet, sentimentValue, confidenceLevel)
        
        if confidenceLevel * 100 >= 90:
            output = open("twitterSentiments.txt","a")
            output.write(sentimentValue)
            output.write('\n')
            output.close()
        
        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

firstarg=sys.argv[1]
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[firstarg])
