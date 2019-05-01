# Use: pip install yweather 
# This package uses the Yahoo RSS feed for weather, geolocation, WOEID, and more

# Imports
import yweather
import argparse

# CMD Interface using argparse
parser = argparse.ArgumentParser()
parser.add_argument('-W', help='Gets the WOEID for a location', action='store_true') # Get WOEID
args = parser.parse_args()

if args.W:
        # Creating an object
        client = yweather.Client()

        # User Input
        user_location = str(input('Enter location: '))
        ##print(user_location)

        # Get WOEID
        print(client.fetch_woeid(user_location)) # Prints WOEID number
