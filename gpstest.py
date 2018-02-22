import gpsd, time
gpsd.connect()
while True:
    packet = gpsd.get_current()
    print(packet.position())
    time.sleep(5)
