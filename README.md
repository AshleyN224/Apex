# GeoTweets by Team Apex
## Developers
Michael Dailey, Jenisha Khanal, Ashley Newsome 
<!--Sorted in alphabetical order-->

## Contributions
https://github.com/ITM-S19/Apex



## Dependencies (potential subsection for program design)

#### Standard Built-In Libraries
- sys
- json
- collections

#### Third Party Libraries 
- [Tweepy](https://github.com/tweepy/tweepy)
- [Yweather](https://github.com/tsroten/yweather)
- [Pyfiglet](https://github.com/pwaller/pyfiglet)

#### Local Modules
- auth


## Support
For any help regarding issues, questions, or concerns, please feel free to contact The Apex Group, Inc. 

---
---
# Introduction 
For our program, we will write a script that will help users find Twitter trends based on geolocation. They will be able to enter the area (US cities and countries ) of their choice and the program will provide the top trending searches and hashtags for that particular location. 

The pseudo code will work as follows: 
- Call the program with US cities or countries.
- Fetch Where on Earth ID (WOEID) using yweather library
- Make twitter GET trends/place request to find top 50 trends based on WOEID
  - Data comes in json    
- Parse json and sort by tweet_volume
- Display top trends to the screen 
- export the results to .txt file

---

## Motivation
Our program will revolutionize the way in which Twitter users find out about and follow trends. Currently, Twitter showcases trends varied by subject (news, sports, entertainments) and it is personalized based on where the user is located. While this is great, our program will further globalize Twitter user interface and allow for users to advance timeline personalization and shape it exactly how they want, not limited to the area in which they live. 

This is useful because people might desire to keep up with the popular culture of other places in the world, maybe where they’re from or where they are headed. Formal news platforms do exist and allow them to keep up with currents events in various places and so on but Twitter provides them with the real-time, quotidian news that may not be substantial enough for formal news platforms to broadcast but are significant indicators of the everyday culture of the area.

---

## Program Description

***Description goes here***

---

## Program Design

#### How the program works
GeoTweets utilizes the module `yweather` to fetch Where On Earth IDs (WOEID). WOEIDs are numerical representations of geographical locations. The Trends/Places Twitter API endpoint requires a WOEID parameter to fetch `trends.json`. The GET request is done using the API wrapper `tweepy`. `trends.json` will show the top 50 trends from the given WOEID location. This is a sample dictionary entry in the .json output:

        {
        "name": "#MetGala",
        "url": "http://twitter.com/search?q=%23MetGala",
        "promoted_content": null,
        "query": "%23MetGala",
        "tweet_volume": 5456689
        }

GeoTweets only accesses `name` and `tweet_volume` to display data to the user, sorted in descending order of tweet volume. 

`tweet_volume` is not indicative of the amount of tweets from the given location. It is instead the global amount of tweets in a trend for the last 24 hours. This program will display _which_ trends are popular in an area. Two different regions can have the same trends but at different rankings. However, the trends will have the same tweet volume in both locations, regardless of their rank.

Some trends found in `trends.json` will have `tweet_volume` set to `null`. This means that the Twitter API does not have any data available for the given trend. This program will automatically sort out any trends in which: 
> "tweet_volume": null

As a result, not all 50 trends will be displayed to the user. How many are displayed are soley dependant on how many trends returned with integers for `tweet_volume` and vary from location to location.

---

#### The usage options of this program are as follows:

Get top trends of a geographical location:
> `python geotweets.py -trends`
>
> OR
>
> `python geotweets.py -trends [city | country]`

Fetch Where On Earth ID (WOEID) of a geographical location:
> `python geotweets.py -woeid`
> 
> OR
> 
> `python geotweets.py -woeid [city | country]`

Enter command line interface of the program:
> `python geotweets.py`
> 
Note: Locations that have more than one word should be put in quotes. Example:
> `python geotweet.py -trends 'Los Angeles'`

--- 
`python geotweets.py` will launch a command line interface version of GeoTweets. The user can loop through the program multiple times using this method. The interface is as follows:
    
    > python geotweets.py  
    --------------------------------------------------
    ____          _____                   _       
    / ___| ___  __|_   _|_      _____  ___| |_ ___ 
    | |  _ / _ \/ _ \| | \ \ /\ / / _ \/ _ \ __/ __|
    | |_| |  __/ (_) | |  \ V  V /  __/  __/ |_\__ \
    \____|\___|\___/|_|   \_/\_/ \___|\___|\__|___/
                                                    

    --------------------------------------------------

    What would you like to do?
    (1) Get trends
    (2) Get WOEID
    (3) Exit program

---
### Authentication

`tweepy` handles authentication by using its built-in modules `OAuthHandler`  and `set_access_token`. All authentication is done in `auth.py` where the object `api` is instantiated and will be used for making authenticated API calls. `api` is imported to `geotweets.py` to make the `trends_places` function call.  Ordinarily the keys:

`consumer_key`,
`consumer_secret`,
`access_token`,
`access_token_secret`,

should not have have their values included in the code posted to GitHub, but for the purposes of this educational project they are left in for the professor.

---
