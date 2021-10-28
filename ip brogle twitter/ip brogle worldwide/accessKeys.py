import tweepy

CONSUMER_KEY = 'NASxnvHTI7agZxKXgNCY8eipk'
CONSUMER_SECRET = '8Xxe8tPuVlg9JlWX6rgsGhe3CbWpWftCVzc0Nb3IY0OXoj93T2'
ACCESS_KEY = '1390168076792991744-qY5UY8bcSnr8QS4bLZVSJrE7pCzR1w'
ACCESS_SECRET = 'ko1PKUyGovbWqZ6sWIZqKw2riWvXGosaXkFsNEmduUA6Z'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)