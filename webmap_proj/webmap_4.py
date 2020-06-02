import folium
import pandas as pd

my_map4 = folium.Map(location=[35.967230, -86.826080], zoom_start=15, tiles='Stamen Terrain')

df = pd.read_csv('volcanoes_usa.txt')

# we need to add elevation as an iterator in the for loop

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    # for specific elevation make color as y
    # but the color is inside a method so need to use inline statements

    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color='green' if elev in range(0, 1000) else 'orange' if elev in range(1001, 1999) else'blue' if elev in range(2000, 2999) else 'red', icon='cloud')).add_to(my_map4)

print(my_map4.save('test5.html'))
