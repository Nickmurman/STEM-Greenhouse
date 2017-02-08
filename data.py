#TODO make packageable
"""
This module handles all the data incoming and writes it to a file.
"""
from time import sleep
import datetime
import serial

DATA_SOURCE = {
1 : 'AdTemp1', 2 : 'AdTemp2', 3 : 'AdTemp3', 4 : 'AdTemp4', 5 : 'AdTemp5',
6 : 'AdHumid1', 7 : 'AdHumid2', 8 : 'AdHumid3', 9 : 'AdHumid4', 10 : 'AdHumid5'}

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

#Selecting all the files that will be used to record data
TEMPFILE_1 = open('data/artemps1.txt', 'r+')
TEMPFILE_2 = open('data/artemps2.txt', 'r+')
TEMPFILE_3 = open('data/artemps3.txt', 'r+')
TEMPFILE_4 = open('data/artemps4.txt', 'r+')
TEMPFILE_5 = open('data/artemps5.txt', 'r+')

HUMIDFILE_1 = open('data/arhumids1.txt', 'r+')
HUMIDFILE_2 = open('data/arhumids2.txt', 'r+')
HUMIDFILE_3 = open('data/arhumids3.txt', 'r+')
HUMIDFILE_4 = open('data/arhumids4.txt', 'r+')
HUMIDFILE_5 = open('data/arhumids5.txt', 'r+')

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

SER1 = serial.Serial('/dev/ttyUSB0', 9600)
SER2 = serial.Serial('/dev/ttyUSB1', 9600)
SER3 = serial.Serial('/dev/ttyUSB2', 9600)
SER4 = serial.Serial('/dev/ttyUSB3', 9600)

while True:
    COUNTER = 0
    #Make sure the date recorded for the data is the current time
    DATETIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        #Convert the data from the serial buffer into a normal string
        CURRENT_HUMID_1 = str(SER1.readline().decode().strip())
        HUMIDSTORAGE_1.append(CURRENT_HUMID_1)
    except IOError:
        print("Error: Arduino 1 didn't send data when requested.")

    try:
        CURRENT_HUMID_2 = str(SER2.readline().decode().strip())
        HUMIDSTORAGE_2.append(CURRENT_HUMID_2)
    except IOError:
        print("Error: Arduino 2 didn't send data when requested.")

    try:
        CURRENT_HUMID_3 = str(SER3.readline().decode().strip())
        HUMIDSTORAGE_3.append(CURRENT_HUMID_3)
    except IOError:
        print("Error: Arduino 3 didn't send data when requested.")

    try:
        CURRENT_HUMID_4 = str(SER4.readline().decode().strip())
        HUMIDSTORAGE_4.append(CURRENT_HUMID_4)
    except IOError:
        print("Error: Arduino 4 didn't send data when requested.")

        #TODO Figure out how to read data correctly twice from one arduino.
        #CURRENT_HUMID_5 = str(SER5.readline().decode().strip())

    try:
        CURRENT_TEMP_1 = str(SER1.readline().decode().strip())
        TEMPSTORAGE_1.append(CURRENT_TEMP_1)
    except IOError:
        print("Error: Arduino 1 didn't send data when requested.")

    try:
        CURRENT_TEMP_2 = str(SER2.readline().decode().strip())
        TEMPSTORAGE_2.append(CURRENT_TEMP_2)
    except IOError:
        print("Error: Arduino 2 didn't send data when requested.")

    try:
        CURRENT_TEMP_3 = str(SER3.readline().decode().strip())
        TEMPSTORAGE_3.append(CURRENT_TEMP_3)
    except IOError:
        print("Error: Arduino 3 didn't send data when requested.")

    try:
        CURRENT_TEMP_4 = str(SER4.readline().decode().strip())
        TEMPSTORAGE_4.append(CURRENT_TEMP_4)
    except IOError:
        print("Error: Arduino 4 didn't send data when requested.")

    #CURRENT_TEMP_5 = str(SER5.readline().decode().strip())

    if COUNTER >= 10:
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
