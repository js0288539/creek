# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:30:32 2020

@author: owner
"""

### Chapter 16 - Downloading Data

#%% 
## MODULE: sitka_highs.py

#%%
## IMPORT
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import json

## WORLD MAP
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#%%
## DEFINES

filename = r'F:/Public/Creek/Rich/LocLib/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv'
dates, highs,lows = [],[],[]

#%%
## FUNCTIONS

#%%
## CLASSES

#%%
## MAIN
## GET EXTERNAL DATA

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(highs)

#%%
## MAIN PLOT EXTERNAL DATA

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c='blue')
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# format plot
ax.set_title('Daily High Temperatures, July 2018', fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


#%% MODULE: SELF STUDY  - DOWNLOAD FOR READING, PA

filename = r'F:/Public/Creek/Rich/LocLib/READING_PA_2105747.csv'
data, dates, highs,lows = [],[],[],[]

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        data.append(row)
        
#%%
## MODULE: JSON LIBRIES

filename=r'F:/Public/Creek/Rich/LocLib/chapter_16/mapping_global_data_sets/data/eq_data_30_day_m1.json'
with open(filename) as f:
          all_eq_data = json.load(f)

# readable_file = r'F:/Public/Creek/Rich/LocLib/readable_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_date,f,indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
#%%

mags,lons,lats,hover_texts = [],[],[],[]

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:10])
print(lons[:5])
print(lats[:5])

#%% MODULE: WORLD MAP

# data = [Scattergeo(lon=lons,lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Bluered',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'}
        }
    }]
my_layout = Layout(title='Global Earthquakes')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')

#%%

from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)
