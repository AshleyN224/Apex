# TO DO: 
# output to .txt file
# add exception handling for locations not covered by API

## Imports

import sys
import json
from collections import OrderedDict

import pyfiglet # ascii art
import yweather # used for fetching WOEID

from auth import api

## functions

def usageOptions():
    '''Display usage options to user on invalid input or when -h is called.'''
    print('\nUsage options\n'
        +'- Get top trends of a geographical location:\n'
        +'\tpython geotweets.py -trends\n'
        +'\tpython geotweets.py -trends [city | country]\n\n'
        +'- Fetch Where On Earth ID (WOEID) of a geographical location:\n'
        +'\tpython geotweets.py -woeid\n'
        +'\tpython geotweets.py -woeid [city | country]\n\n'
        +'- Enter command line interface of the program:\n'
        +'\tpython geotweets.py')

def getWoeid(location):
    '''Fetches Where On Earth ID of a given location.'''
    client = yweather.Client()
    return client.fetch_woeid(location)

def geoTweets(woeid):
    '''
    Uses Twitter trends/place API endpoint to fetch top trends in a given location.

    Location is determined by using Where On Earth ID (WOEID) from yweather. 
    Yweather will take a user string of a city or country. Twitter will only
    supply trends.json information for 467 WOEIDs. 

    Tweepy sends the GET request for the trends.json file, displaying information about
    the top 50 trends in a given location. This program focuses only on trend names and
    tweet_volume from the .json. Twitter API will return 'None' for some trends, 
    this program will eliminate those trends so that the top trends can be sorted by descending
    tweet volume.

    Each trend that has a tweet_volume != None will be added to a dictionary, which is then sorted
    using OrderedDict. The sorted dictionary gets printed to the user.
    '''

    client = yweather.Client()
    
    # api call for trends/place endpoint resulting in json output
    tmp = api.trends_place(woeid) # one list of dictionaries in json format 
    data = tmp[0] # just the dictionaries from the overall large list 

    # dump json data from api request to .json file
    with open('trend_data.json', 'w') as outfile:  
        json.dump(data, outfile)    
    
    # header for data being displayed
    print('\nTop Twitter trends as of {} in {}.'.format(data['as_of'][:10], data['locations'][0]['name']))
    print('\n   {:>20}:\t{}\n'.format('Trend','Tweet Volume') + '-'*40)

    # put trends where tweet_volume is an int and not null into dictionary
    d = {}
    for x in range(50):
        if data['trends'][x]['tweet_volume'] != None:
            d[data['trends'][x]['name']] = data['trends'][x]['tweet_volume']
        else:
            pass

    # sort tweets dictionary by descending tweet_volume
    sortDict = OrderedDict(sorted(d.items(), key=lambda t: t[1],reverse=True))
    count = 1
    for k, v in sortDict.items():
        print('{:02}) {:>20}:\t{:,}'.format(count, k,v))
        count += 1

    print('-'*40) # padding

## main

# give greeting and prompt user for inputs 
if len(sys.argv) == 1:
    # ascii art greeting
    art = pyfiglet.figlet_format("World of Tweets", font = "5lineoblique" ) 
    print(art)
    print('*' * 75)
    
    # loop that prompts user what they would like to do
    while True:
        choice = input('\nWhat would you like to do?\n(1) Get trends\n(2) Get WOEID\n(3) Exit program\n\nEnter number: ')
        
        if choice == '1':
            geoTweets(getWoeid(str(input('Enter location: '))))
        
        elif choice == '2':
            print('WOEID:', getWoeid(str(input('Enter location: '))))

        elif choice == '3':
            print('Exiting. Goodbye!')
            sys.exit()

        else:
            print('Input not recognized. Select a valid input.')

# display usage options
elif sys.argv[1] == '-h':
    usageOptions()

# get trends and tweet_volume
elif sys.argv[1] == '-trends':
    # when user provides location via CLI
    if len(sys.argv) == 3:
        woeid = getWoeid(sys.argv[2])
        geoTweets(woeid)

    # when user does not provide location via CLI
    elif len(sys.argv) == 2:
        woeid = getWoeid(str(input('Enter location: ')))
        geoTweets(woeid)

elif sys.argv[1] == '-woeid':
    #  when user provides location via CLI
    if len(sys.argv) == 3:
        print('WOEID:',getWoeid(sys.argv[2]))

    #  when user does not provide location via CLI
    elif len(sys.argv) == 2:
        print('WOEID:', getWoeid(str(input('Enter location: '))))

else:
    print('Input not recognized. use the -h flag for usage instructions.')
