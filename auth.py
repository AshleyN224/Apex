import tweepy

# set keys for authentication
# Keys are used to add authentication, but are removed for security purposes as this is a public repo.
consumer_key = 'XXXX' 
consumer_secret = 'XXXX' 
access_token = 'XXXX'
access_token_secret = 'XXXX'

# set authentication used by tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create tweepy object with authentication
api = tweepy.API(auth)