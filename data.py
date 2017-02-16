#TODO make packageable
"""
This module handles all the incoming data and writes it to a file as well as
creating graphs.
"""
from time import sleep
import datetime
import serial
import pygal
import logging

#Configuring Logging
#logging.basicConfig(filename='data.log', level=logging.DEBUG,
#format='%(asctime)s' '%(message)s')

#Establishing the Data Sources for the data
DATA_SOURCE = {
    "T1" : 'TempSen1', "T2" : 'TempSen2', "T3" : 'TempSen3', "T4" : 'TempSen4',
    "H1" : 'HumidSen1', "H2" : 'HumidSen2', "H3" : 'HumidSen3', "H4" : 'HumidSen4'}

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
#    logging.warning(' Warning, Sensor %s didn\'t send data when requested', ardnum)
    pass
#Establish the correct serial buffer for each sensor and graph
# THSER = serial.Serial(, 9600)
# WSER = serial.Serial(, 9600)

#Selecting all the files that will be used to record data
TEMPFILE_1 = open('data/ardtemps1.txt', 'r+')
TEMPFILE_2 = open('data/ardtemps2.txt', 'r+')
TEMPFILE_3 = open('data/ardtemps3.txt', 'r+')
TEMPFILE_4 = open('data/ardtemps4.txt', 'r+')

HUMIDFILE_1 = open('data/ardhumids1.txt', 'r+')
HUMIDFILE_2 = open('data/ardhumids2.txt', 'r+')
HUMIDFILE_3 = open('data/ardhumids3.txt', 'r+')
HUMIDFILE_4 = open('data/ardhumids4.txt', 'r+')


TEMPSTORAGE_1 = []
TEMPSTORAGE_2 = []
TEMPSTORAGE_3 = []
TEMPSTORAGE_4 = []

HUMIDSTORAGE_1 = []
HUMIDSTORAGE_2 = []
HUMIDSTORAGE_3 = []
HUMIDSTORAGE_4 = []

TIMESTORAGE = []

def start_reading_data():
    while True:
        COUNTER = 0
        #Make sure the date recorded for the data is the current time
        DATETIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        TIMESTORAGE.append(DATETIME)
        try:
            CURRENT_LINE = SER.readline().decode().strip()
        except IOError:
            logging.error("Error, no data received")

        try:
            if CURRENT_LINE[3] == '1':
                if CURRENT_LINE[5] == 'H':
                    HUMID = DataSet(DATA_SOURCE["H1"], CURRENT_LINE[7:12], DATETIME)
                    HUMID_STORAGE.append(HUMID)
                elif CURRENT_LINE[5] == 'T':
                    TEMP = DataSet(DATA_SOURCE["T1"], CURRENT_LINE[7:12], DATETIME)
                    TEMP_STORAGE.append(TEMP)
                else:
                    log_serial_error(1)
            if CURRENT_LINE[3] == '2':
                if CURRENT_LINE[5] == 'H':
                    HUMID = DataSet(DATA_SOURCE["H2"], CURRENT_LINE[7:12], DATETIME)
                    HUMID_STORAGE.append(HUMID)
                elif CURRENT_LINE[5] == 'T':
                    TEMP = DataSet(DATA_SOURCE["T2"], CURRENT_LINE[7:12], DATETIME)
                    TEMP_STORAGE.append(TEMP)
                else:
                    log_serial_error(2)
            if CURRENT_LINE[3] == '3':
                if CURRENT_LINE[5] == 'H':
                    HUMID = DataSet(DATA_SOURCE["H3"], CURRENT_LINE[7:12], DATETIME)
                    HUMID_STORAGE.append(HUMID)
                elif CURRENT_LINE[5] == 'T':
                    TEMP = DataSet(DATA_SOURCE["T3"], CURRENT_LINE[7:12], DATETIME)
                    TEMP_STORAGE.append(TEMP)
                else:
                    log_serial_error(3)
            if CURRENT_LINE[3] == '4':
                if CURRENT_LINE[5] == 'H':
                    HUMID = DataSet(DATA_SOURCE["H4"], CURRENT_LINE[7:12], DATETIME)
                    HUMID_STORAGE.append(HUMID)
                elif CURRENT_LINE[5] == 'T':
                    TEMP = DataSet(DATA_SOURCE["T4"], CURRENT_LINE[7:12], DATETIME)
                    TEMP_STORAGE.append(TEMP)
                else:
                    log_serial_error(4)
        except IOError:
            logging.error('Error, Arduino didn\'t send data when requested.')

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
        TEMP_CHART.add('Sensor 1', TEMPSTORAGE_1)
        TEMP_CHART.add('Sensor 2', TEMPSTORAGE_2)
        TEMP_CHART.add('Sensor 3', TEMPSTORAGE_3)
        TEMP_CHART.add('Sensor 4', TEMPSTORAGE_4)
        TEMP_CHART.render_to_png('/home/aegon/Documents/STEM-Greenhouse/templates/tempchart.png')

        HUMID_CHART = pygal.Line(style=DarkStyle, width=1600, height=800,
        range=(10, 91))
        HUMID_CHART.title = 'Humidity Chart for the Last Hour'
        HUMID_CHART.x_labels = map(str, TIMESTORAGE)
        HUMID_CHART.add('Sensor 1', HUMIDSTORAGE_1)
        HUMID_CHART.add('Sensor 2', HUMIDSTORAGE_2)
        HUMID_CHART.add('Sensor 3', HUMIDSTORAGE_3)
        HUMID_CHART.add('Sensor 4', HUMIDSTORAGE_4)
        HUMID_CHART.render_to_png('/home/aegon/Documents/STEM-Greenhouse/templates/humidchart.png')

        HUMIDSTORAGE_1.clear()
        HUMIDSTORAGE_3.clear()
        HUMIDSTORAGE_2.clear()
        HUMIDSTORAGE_4.clear()

        TEMPSTORAGE_1.clear()
        TEMPSTORAGE_2.clear()
        TEMPSTORAGE_3.clear()
        TEMPSTORAGE_4.clear()

    COUNTER += 1
    sleep(1)
