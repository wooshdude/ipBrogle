from accessKeys import *
import tweepy
import time
import random
import ipBrogle

tweetNumber = 20
q = "@ipbrogle"
tweets = api.search_tweets(q, count = 10, result_type = 'recent')


def crashBot():
    for tweet in reversed(tweets):
            if q in tweet.text.lower():
                print(str(tweet.text))
                with open("tweetIDs.txt", 'r+') as f:
                    textFile = f.readlines()
                    print(textFile)
                    if f'{tweet.id}\n' not in textFile:
                        ipBrogle.generateIp()
                        api.update_status_with_media(status=f'@{tweet.user.screen_name}', filename='result.jpg', in_reply_to_status_id=tweet.id)

                        f.write(f'{tweet.id}\n')
                    else:
                        print("tweet has already been responded to")

                
                
                print("done!")


while True:
    crashBot()
    time.sleep(5)
