
import os
import json
import pandas as pd
import seaborn as sns
from time import sleep
import numpy as np
import matplotlib.pyplot as plt


all_yrs = []
path = 'venv/yearly_info'
for file in os.listdir(path):
    with open(path+'/'+file) as f:
        data = json.load(f)
        all_yrs.append(data)


all_yr_song = []
for yr in all_yrs:
    chart_info = yr['info']
    for song in chart_info:
        song['year'] = yr['year']
        all_yr_song.append(song)


def main_artist(s):
    s = str(s)
    main = s.strip()
    if 'Featuring' in s:
        main = s.split('Featuring')[0].strip()

    if 'With' in s:
        main = s.split('With')[0].strip()

    return main

def search_for_song(artist):
    """
    search for results by artist
    """
    result = songs_df.loc[songs_df['main_artist'] == artist]
    return result


# ######## get top 20
songs_df = pd.DataFrame.from_dict(all_yr_song, orient='columns')
songs_df['main_artist'] = songs_df.artist.apply(main_artist)
songs_df["year"] = pd.to_numeric(songs_df["year"])
#
artist_song_df = songs_df[['main_artist','song']]
all_time_count = artist_song_df.groupby('main_artist').count().reset_index()
all_time_count = all_time_count.sort_values('song')
#
#
count_by_artist = artist_song_df.groupby('main_artist').count().reset_index()
count_by_artist = count_by_artist.sort_values('song')
count_by_artist = count_by_artist.tail(20) #top 20
#
# sns.set(style="whitegrid")
# g = sns.barplot(x='main_artist',y='song',data=count_by_artist)
# g.set(ylabel='# of Songs on Top 100 Year End Charts', xlabel='Artist')
#
# g.set_xticklabels(g.get_xticklabels(),rotation=30)
# ##################




import matplotlib
import matplotlib.pyplot as plt

years = 1985
df_list = []
while years < 2020:

    yearly_increment = songs_df[songs_df.year < years]

    artist_song_df = yearly_increment[['main_artist', 'song']]
    count_by_artist = artist_song_df.groupby('main_artist').count().reset_index()
    count_by_artist = count_by_artist.sort_values('song')
    count_by_artist = count_by_artist.tail(20)  # top 20

    df_list.append(count_by_artist)
    years = years + 1












from matplotlib.pyplot import figure
from pylab import MaxNLocator


yr = 1985
ax = plt.figure(num=None, figsize=(14, 10), dpi=80, facecolor='w', edgecolor='b').gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(False)
ax.set_xlabel("# Of Times on Billboard's Year End Top 100")
#ax.set_ylabel("Artist")
plt.gcf().subplots_adjust(left=0.20)
plt.gcf().subplots_adjust(bottom=0.14)

for i in df_list:
    #figure(num=None, figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
    plt.tight_layout()
    plt.grid(False)
    plt.gcf().subplots_adjust(left=0.20)
    plt.gcf().subplots_adjust(bottom=0.14)

    yr_str = 'Year %s' % yr
    plt.figtext(0.76, 0.18, yr_str, fontsize=32, fontweight='bold',color='lightslategray')

    plt.figtext(0.02, 0.7, 'Artist', fontsize=14, fontweight='bold',rotation=90)

    plt.xticks(rotation=60)
    #plt.xlabel("# Of Times on Billboard's Year End Top 100", fontsize=14, fontweight='bold')
    plt.figtext(0.38, 0.07, "# Of Times on Billboard's Year End Top 100", fontsize=14, fontweight='bold')
    #plt.ylabel("Artist")
    plt.barh(i['main_artist'], i['song'], color='slategray')

    plt.yticks(fontsize=13)

    plt.pause(.4)
    if yr < 2019:
        plt.clf()

    yr = yr + 1

plt.show()
