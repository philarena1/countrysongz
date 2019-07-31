import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import json
import os
from random import random, randint



song_df = pd.read_csv('venv/kacey.csv')

# format songs for url
song_df['url_song']= song_df['song'].str.lower()
song_df['url_song'] = song_df['url_song'].str.replace(' ','')
song_df['url_song'] = song_df['url_song'].str.replace(',','')
song_df['url_song'] = song_df['url_song'].str.replace("'",'')
song_df['url_song'] = song_df['url_song'].str.replace("&",'')


artist_name = 'kaceymusgraves'

def get_url(string):
    url = "https://www.azlyrics.com/lyrics/%s/%s.html" % ( str(artist_name),str(string))
    return url

song_df['lyrics_url'] = song_df['url_song'].apply(get_url)



def get_song_lyrics(url):
    print('getting lyrics from %s' % url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    lyrics = str(soup.find_all("div", limit=22)[-1])
    lyrics = lyrics.replace(
        '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->',
        '')
    lyrics = lyrics.replace('<div>', '')
    lyrics = lyrics.replace('<br/>', '')
    lyrics = lyrics.replace('</div>', '')
    lyrics = lyrics.replace('\n', ' ')
    lyrics = lyrics.replace('\r', ' ')

    # wait a bit
    rand_wait = float(randint(9, 20)) + float(random())
    print('waiting %s seconds' % str(rand_wait))
    sleep(rand_wait)

    return lyrics


song_df['song_lyrics'] = song_df['lyrics_url'].apply(get_song_lyrics)

song_df.to_csv('venv/kacey.csv')




