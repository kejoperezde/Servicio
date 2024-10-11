import serial
import time

# Configura el puerto y la velocidad
puerto = '/dev/ttyUSB0'  # Cambia esto al puerto correspondiente (ej. '/dev/ttyUSB0' en Linux)
velocidad = 9600  # Asegúrate de que coincida con la configuración del receptor

try:
    # Abre el puerto serial
    with serial.Serial(puerto, velocidad, timeout=1) as ser:
        print(f"Conectado a {puerto} a {velocidad} baudios")
        time.sleep(2)  # Espera a que la conexión se establezca

        while True:
            if ser.in_waiting > 0:  # Comprueba si hay datos en el búfer
                datos = ser.readline().decode('utf-8').rstrip()  # Lee una línea
                print(f"Datos recibidos: {datos}")
                
except serial.SerialException as e:
    print(f"Error al abrir el puerto: {e}")
except KeyboardInterrupt:
    print("Interrupción por el usuario, cerrando.")
