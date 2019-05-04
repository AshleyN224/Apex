# TO DO: 
# Sort trends by their tweet volume
# Convert to dataframe and output to .txt file

# Use: pip install fire (fire is a new CLI created by Google in 2017)

# Imports
import yweather # This package uses the Yahoo RSS feed for weather, geolocation, WOEID, and more
import fire # Python Google Fire (CLI)
import pyfiglet # ASCII art, just because.
import tweepy # Python Twitter wrapper
import json
import pandas as pd

# Greetings
art = pyfiglet.figlet_format("World of Tweets", font = "5lineoblique" ) 
print(art)
pad = 75
print('*' * pad)
        
# Create a class
class World_of_Tweets(object):
    """ Gets WOEID for a location.
    Usage 1: python All_Together.py locations <"location">
    Usage 2: python All_Together.py GeoTweets locate
    Help: python All_Together.py -- --help """

    # Setting up CLI using fire
    def locations(self, locate):
#        """ Gets WOEID for a location.
#        Usage 1: woeid.py <"locatation">
#        Usage 2: woeid.py --locate <"location">
#        Help: woeid.py -- --help """
        # Creating an Object
        client = yweather.Client()
        # User Input
        user_location = '{locate}'.format(locate=locate).upper() # str(input('Enter location:'))
        # Get WOEID
        print(user_location)
        print('WOIED:', client.fetch_woeid(user_location))

# Farewell
#pad = 75
#print('*' * pad)

#########################################################################################################
#########################################################################################################

    def GeoTweets(self, locate):
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
        #woeid = 2466256
        client1 = yweather.Client()
        user_loc = str(input('Enter Location:'))
        getwoeid = client1.fetch_woeid(user_loc)

        # api call for trends/place endpoint resulting in json output
        tmp = api.trends_place(getwoeid) # one list of dictionaries in json format 
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

def main():
    fire.Fire(World_of_Tweets)

# Turns locations into CLI using fire. 
if __name__ == '__main__':
    main()
