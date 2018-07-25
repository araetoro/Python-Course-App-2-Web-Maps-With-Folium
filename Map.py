import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

def color_producer(el):
    if el < 1500:
        return "green"
    elif 1500 <= el <3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[35.58, -99.99], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elv):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function= lambda x: {"fillColor":"green" if x["properties"]["POP2005"]< 10000000
else 'orange' if 10000000 <= x["properties"] ["POP2005"] < 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
