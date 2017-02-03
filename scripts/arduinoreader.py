#TODO make packageable
import serial, pygal, datetime
from time import sleep

dataSource = {
1 : 'AdTemp1',
2 : 'AdTemp2',
3 : 'AdTemp3',
4 : 'AdTemp4',
5 : 'AdTemp5',
6 : 'AdHumid1',
7 : 'AdHumid2',
8 : 'AdHumid3',
9 : 'AdHumid4',
10 : 'AdHumid5'
}

class dataPoint(object):
    """docstring for dataSet."""
    def __init__(self, id, value, time):
        self.id = id
        self.value = float(value)
        self.time = str(time)
    def call(self):
        return self.id, self.value, self.time
    def value(self):
        return self.value


tempstorage = []
humidstorage = []
timestorage = []
temp = []
humid = []
counter = 0

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
except IOError as e:
    ser = serial.Serial('/dev/ttyUSB1', 9600)

while True:
    try:
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        humid = str(ser.readline().decode().strip())
        temp = str(ser.readline().decode().strip())
        humidData = dataPoint(dataSource[6], humid[2:], d)
        humidstorage.append(humidData.value)
        tempData = dataPoint(dataSource[1], temp[2:], d)
        tempstorage.append(tempData.value)
        timestorage.append(d)
        print(humidData.call())
        print(tempData.call())
    except IOError:
        print("Error: Serial device didn't send data when requested.")
    counter += 1
    if counter >= 10:
        print('Generating Graph')
        temp_chart = pygal.Line()
        temp_chart.title = 'Temperature Chart for the Last 10 Readings'
        temp_chart.x_labels = map(str, timestorage)
        temp_chart.add('Arduino 1', tempstorage)
        temp_chart.render_to_svg('/home/aegon/Documents/STEM-Greenhouse/chart.svg')
        counter = 0
