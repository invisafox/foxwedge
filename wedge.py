#!/usr/bin/python

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyS4',
    baudrate=9600,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

#ser.open()
ser.isOpen()
#print("connected to: " + ser.portstr)

ser.write('W\r\n')


time.sleep(1)

out = ''
while ser.inWaiting() > 0:
	out += ser.read(1)

out = out.replace(str(unichr(2)), "")



print out














ser.close()

