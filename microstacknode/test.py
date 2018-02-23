import microstacknode.hardware.gps.l80gps
import time
gps = microstacknode.hardware.gps.l80gps.L80GPS()
time.sleep(2)
while True:
    data = gps.get_gprmc()
    lat = data.get("latitude")
    long = data.get("longitude")
    print(lat,long)
    time.sleep(2)
