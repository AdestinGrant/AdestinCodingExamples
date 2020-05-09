
#program that creates a collage out of the
#top 100 artists billboard chart, and
#pulls the images from the spotify api

import config
import billboard
import spotipy
import spotipy.util as util
import requests
from PIL import Image
from io import BytesIO

#scope for spotify api(irrelevant to search method but authorization
#requires a scope)
scope = 'user-library-read user-read-recently-played'

#spotify authentication
token = util.prompt_for_user_token(config.spotify_username_key, scope, client_id=config.spotify_client_id, client_secret=config.spotify_client_secret, redirect_uri='https://example.com/callback/')

#billboard chart object with desired chart as parameter
chart = billboard.ChartData('artist-100')

#authorized spotify object
sp = spotipy.Spotify(auth=token)

#create an empty image
collage = Image.new('RGB', (1000,500))

#index of chart entry
chartNum = 0

#columns
for i in range(0,1000,100):
    #rows
    for j in range(0,1000,100):

        #searching for the chart entry using spotify API search method
        results = sp.search(q='artist:' + chart[chartNum].artist, type='artist')

        #printing chart entry
        print(chartNum + 1)
        print(chart[chartNum])

        #assigning the url of the image of the chart entry using spotify API
        imgurl = (results['artists']['items'][0]['images'][0]['url'])

        #getting the image url content response using requests
        response = requests.get(imgurl)

        #opening the image using the response content from requests
        img = Image.open(BytesIO(response.content))
        img.thumbnail((100,100))

        #iterating down the chart
        chartNum += 1

        #pasting artist image at position i,j
        collage.paste(img, (j,i))

#showing the image
collage.show()
