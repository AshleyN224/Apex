# Use: pip install yweather 
# This package uses the Yahoo RSS feed for weather, geolocation, WOEID, and more

# Imports
import yweather

# Creating an object
client = yweather.Client()

# User Input
user_city = str(input('Enter city: '))
user_state = str(input('Enter State:'))
user_location = user_city +','+ user_state
##print(user_location)

# Get WOEID
print(client.fetch_woeid(user_location))
