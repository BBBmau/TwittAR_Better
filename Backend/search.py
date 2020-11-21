import config
import tweepy

auth= tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
api = tweepy.API(auth)


tweets = api.search('#codechella', count = 10)

for tweet in tweets:
    print(tweet.text)

