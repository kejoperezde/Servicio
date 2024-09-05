from time import sleep, time
from machine import ADC
import matplotlib.pyplot as plt

# Configuración del ADC
thermistor_pin = ADC(26)

# Variables para almacenar datos
data = []
timestamps = []

# Tiempo de inicio
start_time = time()

# Recolectar datos durante 5 segundos
while time() - start_time < 5:
    thermistor_value = thermistor_pin.read_u16()
    current_time = time() - start_time
    data.append(thermistor_value)
    timestamps.append(current_time)
    sleep(0.1)  # Espera de 0.1 segundos entre lecturas

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(timestamps, data, marker='o', linestyle='-')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor del Termistor')
plt.title('Datos del Termistor durante 5 segundos')
plt.grid(True)
plt.show()
