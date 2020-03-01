#!usr/bin/python

import sys
import datetime
import time
import sqlite3 as sql

import Adafruit_DHT as dht
import Adafruit_BMP.BMP085 as bmp


i = datetime.datetime.now()
day = i.day
month = i.month
year = i.year
hour = i.hour
minute = i.minute

# bmp_sensor = BMP085.BMP085()


def read_hum():
    hum, temp = dht.read_retry(22,16,retries=2,delay_seconds=1)
    return hum

def read_temp():
    hum, temp = dht.read_retry(22,16,retries=2,delay_seconds=1)
    return temp

# def read_press():
  # press = bmp_sensor.read_temperature()
  # return press

while True:
    hum = read_hum()
    temp = read_temp()
    # press = read_press()

    conn = sql.connect("weather_data.db")
    cur = conn.cursor()
    i = datetime.datetime.now()
    day = i.day
    month = i.month
    year = i.year
    hour = i.hour
    minute = i.minute

    cur.execute("""INSERT INTO data(
                day,month,year,hour,minute,temp,hum) VALUES(
                day,month,year,hour,minute,temp,hum
                )""")

    time.sleep(1800)  # 30 min delay
