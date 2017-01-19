#TODO make packageable
import serial

ser = serial.Serial('/dev/ttyUSB0'. 9600)
s = [0]
while True:
    read_serial = ser.readline()
    s[0] = ser.readline()
    print (s[0])
    print (read_serial)
class SerialWriter(object):
    """docstring for SerialWriter."""
    def __init__(self, arg):
        super(SerialWriter, self).__init__()
        self.arg = arg
