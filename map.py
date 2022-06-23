import folium as fo

loction=input()
map=fo.Map()
x=fo.FeatureGroup(name='My map')
x.add_child(fo.Marker(location=['172.2','123'],popup=loction,icon=fo.Icon()))
map.add_child(x)


