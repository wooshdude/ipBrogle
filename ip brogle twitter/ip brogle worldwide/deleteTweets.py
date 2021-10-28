from accessKeys import *
import tweepy
import time
import random
import ipBrogle

tweets = api.user_timeline(screen_name="ipbrogle", count=20)

def crashBot():
    for tweet in reversed(tweets):
            print(tweet.text)
            api.destroy_status(tweet.id)

    print("done!")


crashBot()
