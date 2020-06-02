import folium
import pandas as pd

my_map4 = folium.Map(location=[35.967230, -86.826080], zoom_start=15, tiles='Stamen Terrain')

# read csv file in python and store in a variable

df = pd.read_csv('volcanoes_usa.txt')

# create for loop to read the file dat and add markers.
# we have 2 iterators, so put them in a zip function


for lat, lon, name in zip(df['LAT'], df['LON'], df['NAME']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(icon='cloud')).add_to(my_map4)

print(my_map4.save('test4.html'))
