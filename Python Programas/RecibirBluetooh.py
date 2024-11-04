import serial

# Abre el puerto serial
port = '/dev/rfcomm0'  
baud_rate = 9600       

with serial.Serial(port, baud_rate) as ser:
    print("Conectado a:", port)
    while True:
        if ser.in_waiting > 0:  
            data = ser.readline().decode('utf-8').strip()
            print("Recibido:", data)
