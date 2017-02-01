#TODO make packageable
import serial, pygal

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
    def __init__(self, id, value):
        self.id = id
        self.value = float(value)
    def call(self):
        return str(self.id), str(self.value)

class graphSet(list):
    """docstring for graphSet."""
    def __init__(self, arg):
        super(graphSet, self).__init__()
        self.arg = arg

#TODO Make daily dict generation possible, and make something in order to write the data to the pi.
#def genDaily(date):
#
#    return
# def output():
storage = {}

ser = serial.Serial('/dev/ttyUSB0', 9600)
teststring = str(ser.readline().strip())
teststring = teststring
print(teststring[2])
#TODO make sure the string slices are in the right spots
while True:
    if teststring[2] == 'H':
        storagedict[]
        humidData = dataPoint(dataSource[6], teststring[4:-1])
        print(humidData.call())
        testDict[1] = humidData
    elif teststring[1] == 'T':
        tempData = dataPoint(dataSource[1], teststring[4:])
        print(tempData.call())
        testDict[1] = tempData
    else:
        print('error')
