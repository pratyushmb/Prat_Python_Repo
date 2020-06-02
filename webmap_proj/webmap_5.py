import folium
import pandas as pd

my_map5 = folium.Map(location=[35.967230, -86.826080], zoom_start=15, tiles='Stamen Terrain')
df = pd.read_csv('volcanoes_usa.txt')


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
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color_code(elev), icon='cloud')).add_to(my_map5)

print(my_map5.save('test6.html'))
