import gmplot
from random import choice
import webbrowser
import gpsd
gpsd.connect()
colours = ["red","green","blue","yellow"]
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
gmap = gmplot.GoogleMapPlotter(packet.position()[0], packet.position()[1], 15)
#gmap.scatter(latitudes, longitudes, color = choice(colours) , marker=True)
gmap.scatter(latitudes, longitudes, 'r', marker=True)
gmap.draw("mymap.html")
webbrowser.open("frame.html", new=0)
