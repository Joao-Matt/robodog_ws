

import rospy
from ublox_gps import UbloxGps
import serial

import serial
from ublox_gps import UbloxGps

port = serial.Serial('COM6')
gps = UbloxGps(port)


def run():
    try:
        print("Listening for UBX Messages")
        while True:
            try:
                geo = gps.geo_coords()
                print(f'geo is: {geo}')
                print("Longitude: ", geo.lon)
                print("Latitude: ", geo.lat)
                print("Heading of Motion: ", geo.headMot)
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()