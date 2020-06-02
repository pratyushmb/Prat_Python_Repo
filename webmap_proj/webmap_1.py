import folium  # package to generate map in python

# print(dir(folium))

# create a map object

my_map = folium.Map(location=[35.967230, -86.826080], zoom_start=7)

# need html file out of the map object- to create a map
# so go to the directory and save the html file to open in a browser.

print(dir(folium.Map))
print(my_map.save('test1.html'))

# change zoom to 15 and add tiles and recreate the html file.

my_map2 = folium.Map(location=[35.967230, -86.826080], zoom_start=15, tiles='Stamen Terrain')
print(my_map2)
print(my_map2.save('test2.html'))
