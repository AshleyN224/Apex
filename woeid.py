# note: to use something like -W, a class and methods would have to be made, which can be done.

# Use: pip install fire (fire is a new CLI created by Google in 2017)

# Imports
import yweather # This package uses the Yahoo RSS feed for weather, geolocation, WOEID, and more
import fire # Python Google Fire (CLI)
import pyfiglet # ASCII art, just because.

# Greetings
art = pyfiglet.figlet_format("World of Tweets", font = "5lineoblique" ) 
print(art)
pad = 75
print('*' * pad)

# Setting up CLI using fire
def locations(locate):
    """ Gets WOEID for a location.
    Usage 1: woeid.py <"locatation">
    Usage 2: woeid.py --locate <"location">
    Help: woeid.py -- --help """
    # Creating an Object
    client = yweather.Client()
    # User Input
    user_location = '{locate}'.format(locate=locate).upper() # str(input('Enter location:'))
    # Get WOEID
    print(user_location)
    print('WOIED:', client.fetch_woeid(user_location))

# Turns locations into CLI using fire. 
if __name__ == '__main__':
    fire.Fire(locations)

# Farewell
pad = 75
print('*' * pad)
# Print top 10/25/50 etc tweets here

# Tested:
## "miami"
## "florida"
## "miami florida"
## "miami,florida" -- caused an error
## "new york"
## "new york new york"
## "italy"
## "rome italy"
## "japan"
## "tokyp japan"
## "United States"
## "Mexico"
## -h -- returns a WOEID
## --help
## -- --help