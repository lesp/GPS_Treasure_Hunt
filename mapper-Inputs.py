import gmplot, webbrowser, gpsd, time, subprocess
subprocess.call(["cgps"," &"])
time.sleep(3)
gpsd.connect()
#Locations to find
Tower = (53.8159877,-3.0554085)
Zoo = (53.8157874,-3.0107095)
Amusement_Park = (53.7924182,-3.0556338)
#Add them to a list
latitudes = [Tower[0],Zoo[0],Amusement_Park[0]]
longitudes = [Tower[1],Zoo[1],Amusement_Park[1]]
#Set current position
packet = gpsd.get_current()
print(packet.position())
loc_lat = [packet.position()[0]]
loc_long = [packet.position()[1]]
gmap = gmplot.GoogleMapPlotter(packet.position()[0], packet.position()[1], 20)
gmap.heatmap(loc_lat,loc_long)
gmap.scatter(latitudes, longitudes, 'r', marker=True)
gmap.draw("mymap.html")
webbrowser.open("frame.html", new=0)

while True:
    packet = gpsd.get_current()
    print(packet.position())
    gmap = gmplot.GoogleMapPlotter(packet.position()[0], packet.position()[1], 20)
    gmap.heatmap(loc_lat,loc_long)
    time.sleep(5)
