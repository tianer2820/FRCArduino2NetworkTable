import serial
from serial.tools import list_ports
from networktables import NetworkTables

# NetworkTables.initialize('10.54.51.2')

ports = list_ports.comports()
good_port = ''
for port in ports:
    print(port.name)
    if port.name == 'ttyUSB0':
        good_port = port.device

ser = serial.Serial(good_port, baudrate=115200, timeout=1000)

all_values = {}

while True:
    while ser.inWaiting() > 0:
        buffer = ser.read(3)
        if buffer == b'AIN':
            typ = buffer
            buffer = ser.read(4)
            assert buffer[3] == 10
            pin = buffer[0]
            value = buffer[1] * 256 + buffer[2]
            # print(typ, pin, value)
            all_values['A{}'.format(pin)] = value
        elif buffer == b'DIN':
            typ = buffer
            buffer = ser.read(3)
            assert buffer[2] == 10
            pin = buffer[0]
            value = buffer[1]
            # print(typ, pin, value)
            all_values['D{}'.format(pin)] = value
        else:
            while ser.read() != b'\n':
                pass
        print(all_values)

# table = NetworkTables.getTable('arduino0')
#
# table.putNumber('A0', 100)

