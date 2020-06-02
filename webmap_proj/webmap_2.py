import folium

my_map3 = folium.Map(location=[35.967230, -86.826080], zoom_start=15, tiles='Stamen Terrain')

# add markers to our map

folium.Marker(location=[35.967230, -86.826080], popup='I am lost', icon=folium.Icon(icon='cloud')).add_to(my_map3)

folium.Marker(location=[35.987230, -86.966080], popup='I can see you', icon=folium.Icon(color='green')).add_to(my_map3)

print(my_map3.save('test3.html'))
