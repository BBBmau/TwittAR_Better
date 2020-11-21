import config
import tweepy
import geocoder
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

searchString = "_mastermau_"


cursor = tweepy.Cursor(api.search, q=searchString, count=20, lang="en", tweet_mode='extended')

maxCount =1
count = 0
g
for tweet in cursor.items():
    print()
    print("Tweet Information")
    print("================================")
    print("Text: ", tweet.full_text)
    print("Geo: ", tweet.geo)
    #print("geoLat", tweet.lat)
   # print("geoLong", tweet.long)
    print("Coordinates: ", tweet.coordinates)
    print("Place: ", tweet.place)
    print()

    print("User Information")
    print("================================")
    print("Location: ", tweet.user.location)
    print("Geo Enabled? ", tweet.user.geo_enabled)
    if tweet.coordinates is None:
        result = geocoder.arcgis(tweet.place)
        tweet.place = (result.x, result.y)
    print("geocoder shit",tweet.place)
    count = count + 1
    if count == maxCount:
        break;