import requests
from bs4 import BeautifulSoup
from time import sleep


def strp_text(text):
    text = text.strip()
    return text



def get_hot_country_by_year(year):
    url = 'https://www.billboard.com/charts/year-end/%s/hot-country-songs' % (year)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    song_ls = []
    for x in soup.findAll(class_='ye-chart-item__primary-row'):
        song_artist = {}

        for rank in x.findAll(class_='ye-chart-item__rank'):
            rank = strp_text(rank.text)
            song_artist['rank'] = rank

        for text in x.findAll(class_='ye-chart-item__text'):

            for title in text.findAll(class_="ye-chart-item__title"):
                song = strp_text(title.text)
                song_artist['song'] = song

            for artist in text.findAll(class_="ye-chart-item__artist"):
                artists = strp_text(artist.text)
                song_artist['artist'] = artists

        song_ls.append(song_artist)
    return song_ls



all_yr = []
year_list = [2010,2011,2012]
for year in year_list:
    print('getting year %s ' % str(year))
    dicts = {}
    info = get_hot_country_by_year(year)
    dicts['year'] = year
    dicts['info'] = info
    all_yr.append(dicts)
    sleep(3)
