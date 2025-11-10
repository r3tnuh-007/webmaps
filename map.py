from folium import *

map = Map(location=[32.5805, -99.6750], zoom_start=7, tiles="OpenStreetMap")

#Creating a feature group
fg = FeatureGroup(name="My Map")

fg.add_child(CircleMarker(location=[32.5805, -99.6750], popup="Center of Texas", icon=Icon(color='red', radius=6)))

fg.add_child(GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x:  {"fillColor":"green" if x['properties']['POP2005'] < 10000000
else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000
else "red"}))

map.add_child(fg)
map.add_child(LayerControl())

map.save("map1.html")
