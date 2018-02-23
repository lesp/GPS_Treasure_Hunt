import gmplot, webbrowser, gpsd, time, subprocess
#Setup the port for gpsd and call cgps to ensure that we have a stable GPS signal
#subprocess.call(["sudo"," gpsd"," /dev/ttyS0"," -F"," /var/run/gpsd.sock"])
#subprocess.call(["cgps"," &"])
#Wait 10 seconds to get a signal
time.sleep(10)
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
#Create two lists, for the location lat & long, as heatmap needs an iterable object.
loc_lat = [packet.position()[0]]
loc_long = [packet.position()[1]]
#Centre the map on the user
gmap = gmplot.GoogleMapPlotter(packet.position()[0], packet.position()[1], 20)
#Plot the user position using a heatmap
gmap.heatmap(loc_lat,loc_long)
#Plot where the treasures
gmap.scatter(latitudes, longitudes, 'r', marker=True)
#Draw the map
gmap.draw("mymap.html")
#Open a web browser
webbrowser.open("frame.html", new=0)

while True:
    packet = gpsd.get_current()
    print(packet.position())
    gmap = gmplot.GoogleMapPlotter(packet.position()[0], packet.position()[1], 20)
    gmap.heatmap(loc_lat,loc_long)
    time.sleep(5)
