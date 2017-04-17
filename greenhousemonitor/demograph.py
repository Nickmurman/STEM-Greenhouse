import datetime
import pygal
from pygal.style import DarkStyle
from time import sleep
import random

TIMESTORAGE = []
for x in range(0,9):
    TIMESTORAGE.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sleep(10)
    print("time added")

TEMPSTORAGE_1 = []
TEMPSTORAGE_2 = []
TEMPSTORAGE_3 = []
TEMPSTORAGE_4 = []

HUMIDSTORAGE_1 = []
HUMIDSTORAGE_2 = []
HUMIDSTORAGE_3 = []
HUMIDSTORAGE_4 = []

for x in range(0,10):

    TEMPSTORAGE_1.append(random.randrange(20,31))
    TEMPSTORAGE_2.append(random.randrange(20,31))
    TEMPSTORAGE_3.append(random.randrange(20,31))
    TEMPSTORAGE_4.append(random.randrange(20,31))

    HUMIDSTORAGE_1.append(random.randrange(50,91))
    HUMIDSTORAGE_2.append(random.randrange(50,91))
    HUMIDSTORAGE_3.append(random.randrange(50,91))
    HUMIDSTORAGE_4.append(random.randrange(50,91))

TEMP_CHART = pygal.Line(style=DarkStyle, width=1600, height=800, range=(0, 31))
TEMP_CHART.title = 'Temperature Chart for the Last Hour'
TEMP_CHART.x_labels = map(str, TIMESTORAGE)
TEMP_CHART.add('Sensor 1', TEMPSTORAGE_1)
TEMP_CHART.add('Sensor 2', TEMPSTORAGE_2)
TEMP_CHART.add('Sensor 3', TEMPSTORAGE_3)
TEMP_CHART.add('Sensor 4', TEMPSTORAGE_4)
TEMP_CHART.render_to_png('/home/aegon/Documents/STEM-Greenhouse/demotempchart.png')

HUMID_CHART = pygal.Line(style=DarkStyle, width=1600, height=800, range=(20, 91))
HUMID_CHART.title = 'Humidity Chart for the Last Hour'
HUMID_CHART.x_labels = map(str, TIMESTORAGE)
HUMID_CHART.add('Sensor 1', HUMIDSTORAGE_1)
HUMID_CHART.add('Sensor 2', HUMIDSTORAGE_2)
HUMID_CHART.add('Sensor 3', HUMIDSTORAGE_3)
HUMID_CHART.add('Sensor 4', HUMIDSTORAGE_4)
HUMID_CHART.render_to_png('/home/aegon/Documents/STEM-Greenhouse/demohumidchart.png')
