import requests
from bs4 import BeautifulSoup
from time import sleep


def strp_text(text):
    text = text.strip()
    return text


def get_hot_country_by_year(year):
    print(year)
    url = 'https://www.billboard.com/charts/year-end/%s/hot-country-songs' % (year)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    song_ls = []
    billboard_num = 1
    for x in soup.findAll(class_='ye-chart-item__text'):
        song_artist = {}
        for title in x.findAll(class_="ye-chart-item__title"):
            song = strp_text(title.text)

        for artist in x.findAll(class_="ye-chart-item__artist"):
            artists = strp_text(artist.text)

        song_artist['song'] = song
        song_artist['artist'] = artists
        song_artist['chart_num'] = billboard_num
        song_artist['year'] = year
        song_ls.append(song_artist)
        billboard_num = billboard_num +1
    return song_ls


info = get_hot_country_by_year(2012)

for x in info:
    print(x)


all_yr = []
year_list = [2010, 2011]
for year in year_list:
    dicts = {}
    info = get_hot_country_by_year(year)
    dicts['year'] = year
    dicts['info'] = info
    all_yr.append(dicts)
    sleep(10)
