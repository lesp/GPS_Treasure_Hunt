import gpsd, time
gpsd.connect()
while True:
    packet = gpsd.get_current()
    print(packet.position())
    print(packet.position()[0])
    time.sleep(5)
