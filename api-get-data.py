# TO DO:
# Sort trends by their tweet volume
# incorporate webscrape.py
# potentially incorporate panda

import tweepy # python twitter wrapper
import json
import pandas as import pd

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

# orlando test WOEID
woeid = 2466256

# api call for trends/place endpoint resulting in json output
tmp = api.trends_place(woeid) # one list of dictionaries in json format 
data = tmp[0] # just the dictionaries from the overall large list

# dump json data from api request to .json file
with open('trend_data.json', 'w') as outfile:  
    json.dump(data, outfile)

# FOR TESTING PURPOSES. 
# opens .json file to avoid calling api and hitting rate limits
#with open('trend_data.json') as json_file:  
#    data = json.load(json_file)



# header for data being displayed
print('\nTop Twitter trends as of {} in {}.'.format(data['as_of'][:10], data['locations'][0]['name']))
print('\n{:>15}:\t{}\n'.format('Trend','Tweet Volume') + '-'*40)

# only print trends where tweet_volume is an int and not null.
for i in range(50):
    try:
        print('{:>15}:\t{:,}'.format(data['trends'][i]['name'],data['trends'][i]['tweet_volume']))
    except:
        pass