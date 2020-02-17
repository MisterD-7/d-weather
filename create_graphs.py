#!usr/bin/python

from matplotlib import pyplot as plt
import sqlite3 as sql

conn = sql.connect("weather_data.db")
cur = conn.cursor()

def plot_temp():
    cur.execute("""SELECT temp FROM data
                   WHERE """)
    temps = cur.fetchall()
    plt.plot(day,temps)
    plt.savefig()
