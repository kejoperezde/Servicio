import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Cargar los datos del CSV
df = pd.read_csv('TopSecret/Kevin/muestra4.csv')

# Filtrado de la señal
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Configuración del filtro
fs = 100  # Frecuencia de muestreo (ajusta según sea necesario)
cutoff = 3.0  # Frecuencia de corte

# Filtrar la señal
filtered_signal = lowpass_filter(df['mV'], cutoff, fs)

# Graficar las señales
plt.figure(figsize=(12, 10))

# Gráfica de la señal original
plt.subplot(2, 1, 1)
plt.plot(df['Seg'], df['mV'], label='Señal Original', color='blue')
plt.title('Señal Original')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('mV')
plt.grid()
plt.legend()

# Gráfica de la señal filtrada
plt.subplot(2, 1, 2)
plt.plot(df['Seg'], filtered_signal, label='Señal Filtrada', color='orange')
plt.title('Señal Filtrada')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('mV')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
