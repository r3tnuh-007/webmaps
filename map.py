from folium import *

map = Map(location=[32.5805, -99.6750], zoom_start=7, tiles="OpenStreetMap")

#Creating a feature group
fg = FeatureGroup(name="My Map")

fg.add_child(Marker(location=[32.5805, -99.6750], popup="Center of Texas", icon=Icon(color='red')))

map.add_child(fg)

map.save("map1.html")
