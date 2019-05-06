# TO DO: 
# Sort trends by their tweet volume
# Convert to dataframe and output to .txt file
# display usage options

# Imports

import sys
import json

import pyfiglet # ascii art
import yweather # used for fetching WOEID
import pandas as pd

from auth import api

# functions

def getWoeid(location):
    client = yweather.Client()
    return client.fetch_woeid(location)


def geoTweets(woeid):
    client = yweather.Client()
    
    # api call for trends/place endpoint resulting in json output
    tmp = api.trends_place(woeid) # one list of dictionaries in json format 
    data = tmp[0] # just the dictionaries from the overall large list 

    # dump json data from api request to .json file
    with open('trend_data.json', 'w') as outfile:  
        json.dump(data, outfile)    
    
    # header for data being displayed
    print('\nTop Twitter trends as of {} in {}.'.format(data['as_of'][:10], data['locations'][0]['name']))
    print('\n{:>15}:\t{}\n'.format('Trend','Tweet Volume') + '-'*40)    
    
    # only print trends where tweet_volume is an int and not null.
    for i in range(50):
        try:
            print('{:>15}:\t{:,}'.format(data['trends'][i]['name'],data['trends'][i]['tweet_volume']))

        except:
            pass

    print('-'*40)

# main

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
    print('help')

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
