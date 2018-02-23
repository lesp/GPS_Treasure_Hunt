#!/usr/bin/env python3
import gmplot, subprocess, time, microstacknode.hardware.gps.l80gps
gps = microstacknode.hardware.gps.l80gps.L80GPS()
#Locations to find
Tower = (53.8159877,-3.0554085)
Zoo = (53.8157874,-3.0107095)
Amusement_Park = (53.7924182,-3.0556338)
#Add them to a list
latitudes = [Tower[0],Zoo[0],Amusement_Park[0]]
longitudes = [Tower[1],Zoo[1],Amusement_Park[1]]
#Set current position
time.sleep(2)
data = gps.get_gprmc()
lat = data.get("latitude")
long = data.get("longitude")
print(lat,long)
#Create two lists, for the location lat & long, as heatmap needs an iterable object.
loc_lat = [lat]
loc_long = [long]
#Centre the map on the user
gmap = gmplot.GoogleMapPlotter(lat, long, 20)
#Plot the user position using a heatmap
gmap.heatmap(loc_lat,loc_long)
#Plot where the treasures
gmap.scatter(latitudes, longitudes, 'r', marker=True)
#Draw the map
gmap.draw("mymap.html")
#Open a web browser
subprocess.call(["chromium-browser"," --start-fullscreen"," frame.html"])

while True:
    data = gps.get_gprmc()
    lat = data.get("latitude")
    long = data.get("longitude")
    print(lat,long)
    gmap = gmplot.GoogleMapPlotter(lat, long, 20)
    gmap.heatmap(loc_lat,loc_long)
    time.sleep(5)
