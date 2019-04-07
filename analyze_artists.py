
import os
import json
import pandas as pd


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


songs_df = pd.DataFrame.from_dict(all_yr_song, orient='columns')

