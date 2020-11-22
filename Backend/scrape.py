import config
import tweepy
import time
import pandas as pd

auth= tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

username = '_mastermau_'
count = 15
try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)

    # Pulling information from tweets iterable object
    tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    # Add or remove columns as you remove tweet information
    tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
    print('failed on_status,', str(e))
    time.sleep(3)