import folium
from folium.map import Popup 

city='高雄市'
city_gps=[22.6203348, 120.3120375]
m=folium.Map(location=city_gps, zoom_start=16)
# folium.Map(location=city_gps, Popup=city).add_to(m)
folium.Marker(location=city_gps, popup=city).add_to(m)
m.save("docs/index.html")