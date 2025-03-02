import serial

# Abre el puerto serial
port = '/dev/rfcomm0'  
baudrate = 9600       

ser = serial.Serial(port, baudrate)

ser.write(b'')     # write a string, manda al dispositivo que envíe datos

#ser.write(b'0')     # write a string, manda al dispositivo para que deje de enviar datos
ser.close()
