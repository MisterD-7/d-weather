#!/usr/bin/python

import sys
import datetime
import sqlite3 as sql

# import Adafruit_DHT as dht
# import Adafruit_




conn = sql.connect("weather_data.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE data (
               day integer,
               month integer,
               year integer,
               hour integer,
               minute integer,
               temp real,
               hum real,
               press real
               )""")


# # cur.execute("INSERT INTO data VALUES({},{},{},{},{})".format(day,month,year,hour,minute))
# cur.execute("DELETE FROM data")
# # print(cur.fetchone())
# conn.commit()
# conn.close()
