import serial
import csv
import time

# Configuración del puerto serie y la velocidad
puerto_serie = '/dev/ttyACM0'
baudrate = 115200

try:
    ser = serial.Serial(puerto_serie, baudrate)
    print(f'Conectado a {puerto_serie} a {baudrate} bps')
except serial.SerialException as e:
    print(f'Error al abrir el puerto serie: {e}')
    exit()

# Esperar 2 segundos para hacer la conexión
time.sleep(2)

# Nombre del archivo CSV y ruta
ruta_archivo = '/home/kejoperezde/Documents/muestras.csv'

# Leer datos y guardarlos en el archivo CSV
with open(ruta_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    print('Esperando datos...')
    while True:
        try:
            if ser.in_waiting > 0:
                dato = ser.readline().decode('utf-8').strip()  # Lee y decodifica
                escritor_csv.writerow([dato])  # Guarda cada dato en una nueva fila
                print(f'Dato guardado: {dato}')
        except serial.SerialException as e:
            print(f'Error al leer del puerto: {e}')
            break
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            break
