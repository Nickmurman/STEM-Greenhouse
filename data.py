#TODO make packageable
"""
This module handles all the data incoming and writes it to a file.
"""
from time import sleep
import datetime
import serial
import pygal
import logging

logging.basicConfig(filename='data.log', level=logging.DEBUG)


DATA_SOURCE = {
    1 : 'AdTemp1', 2 : 'AdTemp2', 3 : 'AdTemp3', 4 : 'AdTemp4', 5 : 'AdTemp5',
    6 : 'AdHumid1', 7 : 'AdHumid2', 8 : 'AdHumid3', 9 : 'AdHumid4',
    10 : 'AdHumid5'}

class DataSet(object):
    """
    The Dataset is how the program receives data from the arduinos and records
    them in lists.
    The ID represents what kind of data(temperature/humidity) the program is
    receiving as well as the arduino it is receiving data from.
    The value is the temperature in Celsius or the humidity in %.
    The time is the time that the data was received by the arduino.
    """
    def __init__(self, id, value, time):
        """
        Initalizing all the variables required for the DataSet.
        """
        self.id = id
        self.value = float(value)
        self.time = str(time)
    def call(self):
        """call() simply returns all the values stored in the DataPoint"""
        return self.id, self.value, self.time

def log_serial_error(ardnum):
    logging.warning('Warning, Arduino %s didn\'t send data when requested', ardnum)

#Selecting all the files that will be used to record data
TEMPFILE_1 = open('data/ardtemps1.txt', 'r+')
TEMPFILE_2 = open('data/ardtemps2.txt', 'r+')
TEMPFILE_3 = open('data/ardtemps3.txt', 'r+')
TEMPFILE_4 = open('data/ardtemps4.txt', 'r+')
TEMPFILE_5 = open('data/ardtemps5.txt', 'r+')

HUMIDFILE_1 = open('data/ardhumids1.txt', 'r+')
HUMIDFILE_2 = open('data/ardhumids2.txt', 'r+')
HUMIDFILE_3 = open('data/ardhumids3.txt', 'r+')
HUMIDFILE_4 = open('data/ardhumids4.txt', 'r+')
HUMIDFILE_5 = open('data/ardhumids5.txt', 'r+')

TEMPSTORAGE_1 = []
TEMPSTORAGE_2 = []
TEMPSTORAGE_3 = []
TEMPSTORAGE_4 = []
TEMPSTORAGE_5 = []

HUMIDSTORAGE_1 = []
HUMIDSTORAGE_2 = []
HUMIDSTORAGE_3 = []
HUMIDSTORAGE_4 = []
HUMIDSTORAGE_5 = []

TIMESTORAGE = []

SER1 = serial.Serial('/dev/ttyUSB0', 9600)
SER2 = serial.Serial('/dev/ttyUSB1', 9600)
SER3 = serial.Serial('/dev/ttyUSB2', 9600)
SER4 = serial.Serial('/dev/ttyUSB3', 9600)

while True:
    COUNTER = 0
    #Make sure the date recorded for the data is the current time
    DATETIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    TIMESTORAGE.append(DATETIME)

    try:
        #Convert the data from the serial buffer into a normal string
        CURRENT_HUMID_1 = str(SER1.readline().decode().strip())
        HUMIDSTORAGE_1.append(CURRENT_HUMID_1)
    except IOError:
        log_serial_error(1)

    try:
        CURRENT_HUMID_2 = str(SER2.readline().decode().strip())
        HUMIDSTORAGE_2.append(CURRENT_HUMID_2)
    except IOError:
        log_serial_error(2)

    try:
        CURRENT_HUMID_3 = str(SER3.readline().decode().strip())
        HUMIDSTORAGE_3.append(CURRENT_HUMID_3)
    except IOError:
        log_serial_error()

    try:
        CURRENT_HUMID_4 = str(SER4.readline().decode().strip())
        HUMIDSTORAGE_4.append(CURRENT_HUMID_4)
    except IOError:
        log_serial_error()

        #TODO Figure out how to read data correctly twice from one arduino.
        #CURRENT_HUMID_5 = str(SER5.readline().decode().strip())

    try:
        CURRENT_TEMP_1 = str(SER1.readline().decode().strip())
        TEMPSTORAGE_1.append(CURRENT_TEMP_1)
    except IOError:
        log_serial_error()

    try:
        CURRENT_TEMP_2 = str(SER2.readline().decode().strip())
        TEMPSTORAGE_2.append(CURRENT_TEMP_2)
    except IOError:
        log_serial_error()

    try:
        CURRENT_TEMP_3 = str(SER3.readline().decode().strip())
        TEMPSTORAGE_3.append(CURRENT_TEMP_3)
    except IOError:
        log_serial_error()

    try:
        CURRENT_TEMP_4 = str(SER4.readline().decode().strip())
        TEMPSTORAGE_4.append(CURRENT_TEMP_4)
    except IOError:
        log_serial_error()

    #CURRENT_TEMP_5 = str(SER5.readline().decode().strip())


    if COUNTER >= 4:
        for x in HUMIDSTORAGE_1:
            HUMIDFILE_1.write(x)
        for x in HUMIDSTORAGE_2:
            HUMIDFILE_2.write(x)
        for x in HUMIDSTORAGE_3:
            HUMIDFILE_3.write(x)
        for x in HUMIDSTORAGE_4:
            HUMIDFILE_4.write(x)


        for x in TEMPSTORAGE_1:
            TEMPFILE_1.write(x)
        for x in TEMPSTORAGE_2:
            TEMPFILE_2.write(x)
        for x in TEMPSTORAGE_3:
            TEMPFILE_3.write(x)
        for x in TEMPSTORAGE_4:
            TEMPFILE_4.write(x)


        TEMP_CHART = pygal.Line(style=DarkStyle, width=1600, height=800,
        range=(0, 31))
        TEMP_CHART.title = 'Temperature Chart for the Last Hour'
        TEMP_CHART.x_labels = map(str, TIMESTORAGE)
        TEMP_CHART.add('Arduino 1', TEMPSTORAGE_1)
        TEMP_CHART.add('Arduino 2', TEMPSTORAGE_2)
        TEMP_CHART.add('Arduino 3', TEMPSTORAGE_3)
        TEMP_CHART.add('Arduino 4', TEMPSTORAGE_4)
        TEMP_CHART.render_to_png('/home/aegon/Documents/STEM-Greenhouse/templates/tempchart.png')

        HUMID_CHART = pygal.Line(style=DarkStyle, width=1600, height=800,
        range=(0, 31))
        HUMID_CHART.title = 'Temperature Chart for the Last Hour'
        HUMID_CHART.x_labels = map(str, TIMESTORAGE)
        HUMID_CHART.add('Arduino 1', TEMPSTORAGE_1)
        HUMID_CHART.add('Arduino 2', TEMPSTORAGE_2)
        HUMID_CHART.add('Arduino 3', TEMPSTORAGE_3)
        HUMID_CHART.add('Arduino 4', TEMPSTORAGE_4)
        HUMID_CHART.render_to_png('/home/aegon/Documents/STEM-Greenhouse/templates/tempchart.png')

    COUNTER += 1
    sleep(1)
        #print('Generating Temp Graph')
        #temp_chart = pygal.Line(style=DarkStyle, width=1600, height=800)
        #temp_chart.title = 'Temperature Chart for the Last 10 Readings'
        #temp_chart.x_labels = map(str, timestorage)
        #temp_chart.add('Arduino 1', tempstorage)
        #temp_chart.render_to_png('/home/aegon/Documents/STEM-Greenhouse/tempchart.png')

        #print('Generating Humid Graph')
        #humid_chart = pygal.Line(style=DarkStyle, width=1600, height=800)
        #humid_chart.title = 'Humidity Chart for the Last 10 Readings'
        #humid_chart.x_labels = map(str, timestorage)
        #humid_chart.add('Arduino 1', humidstorage)
        #humid_chart.render_to_png('/home/aegon/Documents/STEM-Greenhouse/humidchart.png')
        #counter = 0
