import serial

ser = serial.Serial('/dev/rfcomm0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'0')     # write a string
ser.close()             # close port