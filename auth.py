import tweepy

# set keys for authentication
consumer_key = 's3ROZ7S9ptoChaQLp1MCVa5Pr'
consumer_secret = 'oc9IfqrX3L8h9retqkbD3fsR0UcnuW5wG1KYW6K6YtXVWuAmt2'
access_token = '1123324493412356099-F8GXg0wjDzeF1xuLYCOXx2xlaWG0wp'
access_token_secret = 'Ao6PjZv2hml7YOllPCGWq018R36c4ifHaEGq46uGXQ12W'

# set authentication used by tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create tweepy object with authentication
api = tweepy.API(auth)