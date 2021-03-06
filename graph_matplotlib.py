import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import (DAILY, YEARLY, MO, TU, WE, TH, FR, SA, SU,
                                DayLocator, WeekdayLocator, DateFormatter, rrulewrapper, 
                                RRuleLocator, drange, AutoDateLocator,
                                ConciseDateFormatter)
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator, )
import matplotlib.dates as mdates                               
import datetime
import sqlite3
#https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3
print("using MPL version:", matplotlib.__version__)

conn = sqlite3.connect('home_temp.db')
conn.row_factory = lambda cursor, row: row[0] # ezért nem tuple, de csak az első értéket adja tovább. Fazom. :-/
c = conn.cursor()

date_sql = """SELECT datetime(datetime_int, 'unixepoch') FROM bme280_data;"""

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
formatter = DateFormatter('%Y-%m-%d')

locator = AutoDateLocator()
formatter = ConciseDateFormatter(locator)

fig, (ax1) = plt.subplots(1, sharex='all')
fig.autofmt_xdate(rotation=90)

color = 'tab:red'
ax1.plot_date(timestamp, temperature, fmt='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(formatter)
#ax1.xaxis.set_major_locator()
#ax1.xaxis.set_minor_locator(AutoMinorLocator())

ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis
color = 'tab:green'
ax2.plot_date(timestamp, pressure, '.', color=color)
ax2.spines['right'].set_position(('axes', 1.08)) #így kitolom a canvasról, de nincsenek egymáson a skálák
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

plt.grid(True)
plt.subplots_adjust(bottom=0.35, right=0.8, top=0.95) #itt meg atallitom a canvast hogy raferjen mindket skala
#https://matplotlib.org/gallery/axisartist/demo_parasite_axes2.html#sphx-glr-gallery-axisartist-demo-parasite-axes2-py
plt.show()
