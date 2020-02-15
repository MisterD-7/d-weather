#!usr/bin/python

import sys
import time

import Adafruit_DHT as dht
import Adafruit_BMP.BMP085 as bmp

def read_dht():
    hum, temp = dht.read_retry(22,16,retries=2,delay_seconds=1)
    print("Temperatura: {} C | Umidita': {} %".format(temp, hum))


for x in range(10):
    read_dht()
