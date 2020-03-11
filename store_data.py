#!usr/bin/python

import sys
import datetime
import time
import sqlite3 as sql

import Adafruit_DHT as dht
# import Adafruit_BMP.BMP085 as bmp


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

def create_table(cur, create_statement):
	cur.execute(create_statement)

def main():
    while True:
        conn = sql.connect("d-weather.db")
        cur = conn.cursor()

        if conn is not None:
	        cur.execute("""CREATE TABLE IF NOT EXISTS weather(
	                          day INTEGER,
	                          month INTEGER,
	                          year INTEGER,
	                          hour INTEGER,
	                          minute INTEGER,
	                          temperature REAL,
	                          humidity REAL,
	                          pressure REAL);""")


        hum = read_hum()
        temp = read_temp()
    	# press = read_press()

        i = datetime.datetime.now()
        v_day = i.day
        v_month = i.month
        v_year = i.year
        v_hour = i.hour
        v_minute = i.minute

        cur.execute("""INSERT INTO weather(
                	day,month,year,hour,minut,temperature,humidity) VALUES (
                	v_day,v_month,v_year,v_hour,v_minute,temp,hum
                	);""")

        print(temp,hum)

        conn.commit()
        conn.close()

        time.sleep(60)  # 30 min delay

main()
