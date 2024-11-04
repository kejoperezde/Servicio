import serial
import time

# Configura el puerto serie
puerto = '/dev/ttyUSB0'  # Cambia esto según tu sistema (puede ser COM3, COM4, etc. en Windows)
baud_rate = 300  # Asegúrate de que coincida con la configuración del micro Python

# Inicializa la conexión
try:
    ser = serial.Serial(puerto, baud_rate, timeout=1)
    print(f'Conectado a {puerto} a {baud_rate} baudios')
except serial.SerialException as e:
    print(f'Error al abrir el puerto: {e}')
    exit()

# Lee datos en un bucle
try:
    while True:
        if ser.in_waiting > 0:
            # Lee una línea de datos
            datos = ser.read(ser.in_waiting)  # Lee todos los datos disponibles
            try:
                datos_decodificados = datos.decode('utf-8').strip()
                print(f'Datos recibidos: {datos_decodificados}')
            except UnicodeDecodeError:
                print(f'Error de decodificación: {datos}')
        time.sleep(0.1)  # Pequeña pausa para evitar usar demasiado CPU
except KeyboardInterrupt:
    print('Interrupción del usuario, cerrando...')
finally:
    ser.close()
    print('Puerto cerrado')
