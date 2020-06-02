# we would like the map centered around the data and we can average lat and lon
# add an icon color.

import folium
import pandas as pd

df = pd.read_csv('volcanoes_usa.txt')

# take the average
latmean = df['LAT'].mean()
lonmean = df['LON'].mean()

my_map6 = folium.Map(location=[latmean, lonmean], zoom_start=6, tiles='Stamen Terrain')


def color_code(elevtn):
    if elevtn in range(0, 1000):
        col = 'green'
    elif elevtn in range(1001, 1999):
        col = 'blue'
    elif elevtn in range(2000, 2999):
        col = 'orange'
    else:
        col = 'red'
    return col


for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color_code(elev), icon_color='yellow', icon='cloud')).add_to(my_map6)

print(my_map6.save('test7.html'))
