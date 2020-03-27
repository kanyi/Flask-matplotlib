import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import (DAILY, YEARLY, MO, TU, WE, TH, FR, SA, SU,
                                WeekdayLocator, DateFormatter, rrulewrapper, RRuleLocator, drange)
import datetime
import sqlite3
#https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3
print("using MPL version:", matplotlib.__version__)

conn = sqlite3.connect('home_temp.db')
conn.row_factory = lambda cursor, row: row[0] # ezért nem tuple, de csak az első értéket adja tovább. Fazom. :-/
c = conn.cursor()

date_sql = """SELECT datetime(datetime_int, 'unixepoch'), temperature, pressure, humidity  FROM bme280_data;"""

c.execute(date_sql)
#print (c.fetchone())
timestamp = c.fetchall()

c.execute('SELECT temperature FROM bme280_data;')
#print (c.fetchone())
temperature = c.fetchall()

c.execute('SELECT pressure FROM bme280_data;')
#print (c.fetchone())
pressure = c.fetchall()

c.execute('SELECT humidity FROM bme280_data;')
#print (c.fetchone())
humidity = c.fetchall()

print(type(humidity[0]))
#plt.plot_date(temperature, pressure, '.')
#plt.scatter(pressure, humidity)

loc = WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU,))
formatter = DateFormatter('%m-%d')

fig, (ax1) = plt.subplots(1, sharex='all')
#fig.add_axes([0.1, 0.1, 0.6, 0.75],) # ittt kell valamit basztatni, hogy ráférjen két tengely egy oldlra, de így egyenlőre csak egy új, üres canvast tudtam feltenni.

color = 'tab:red'
ax1.plot_date(timestamp, temperature, fmt='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.xaxis.set_major_locator(loc)
ax1.xaxis.set_major_formatter(formatter)

ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis
color = 'tab:green'
ax2.plot_date(timestamp, pressure, '.', color=color)
ax2.spines['right'].set_position(('axes', 1.08)) #baszameg így kitolom a canvasról is.
ax2.tick_params(axis='y', labelcolor=color)
#ax2.xaxis.set_major_locator(loc)
#ax2.xaxis.set_major_formatter(formatter)

color = 'tab:blue'
ax3 = ax1.twinx()
ax3.plot_date(timestamp, humidity, '.', color=color)
ax3.tick_params(axis='y', labelcolor=color)
ax3.set_xlabel('dátum / idő')
#ax3.xaxis.set_major_locator(loc)
#ax3.xaxis.set_major_formatter(formatter)

#plt.xticks([]) #disable xtics
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9) #itt meg atallitom a canvast hogy raferjen mindket skala
#https://matplotlib.org/gallery/axisartist/demo_parasite_axes2.html#sphx-glr-gallery-axisartist-demo-parasite-axes2-py
plt.show()
