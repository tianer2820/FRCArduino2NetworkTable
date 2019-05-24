import serial
from serial.tools import list_ports
from networktables import NetworkTables
import config
import time


if config.SERVER_IP == 'default':
    t0 = config.TEAM // 100
    t1 = config.TEAM % 100
    NetworkTables.initialize('10.{}.{}.2'.format(t0, t1))
else:
    NetworkTables.initialize(config.SERVER_IP)

ports = list_ports.comports()
good_port = ''
for i, port in enumerate(ports):
    print(i, ':', port.name)
    if port.name in config.PORTS:
        good_port = port.device
        break

if good_port == '':
    print('cant find ports listed in config.py, please check.')
    exit(1)

ser = serial.Serial(good_port, baudrate=115200, timeout=1000)
table = NetworkTables.getTable('arduino2nt')

time.sleep(2) # wait for the arduino and the network table

all_values = {}
try:
    while True:
        while ser.inWaiting() > 0:
            buffer = ser.read(3)
            if buffer == b'AIN':
                typ = buffer
                buffer = ser.read(4)
                assert buffer[3] == 10
                pin = buffer[0]
                value = buffer[1] * 256 + buffer[2]

                key = 'A{}'.format(pin)
                # print(typ, pin, value)
                all_values[key] = value
                table.putNumber(key, value)

            elif buffer == b'DIN':
                typ = buffer
                buffer = ser.read(3)
                assert buffer[2] == 10
                pin = buffer[0]
                value = buffer[1]

                key = 'D{}'.format(pin)
                # print(typ, pin, value)
                all_values[key] = value
                table.putBoolean(key, value)

            else:
                while ser.read() != b'\n':
                    pass
            # print(all_values)
except KeyboardInterrupt:
    ser.close()
    print('exit')
except:
    ser.close()
    print('exit')
    raise
