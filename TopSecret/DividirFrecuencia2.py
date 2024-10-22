import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt

# Cargar los datos del CSV
df = pd.read_csv('TopSecret/Kevin/muestra1.csv')

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

fs = 100  # Frecuencia de muestreo (ajusta según sea necesario)
cutoff = 3.0  # Frecuencia de corte
filtered_signal = lowpass_filter(df['mV'], cutoff, fs)

# Detección de picos (picos R)
peaks, _ = find_peaks(filtered_signal, distance=fs*0.6)

# Graficar la señal original
plt.figure(figsize=(12, 6))
plt.plot(df['Seg'], df['mV'], label='Señal Original', alpha=0.5)

# Dividir la señal en componentes P, Q, R, S, T y graficar
for peak in peaks:
    if peak > 0 and peak < len(filtered_signal) - 1:
        # Onda P
        p_wave_start = peak - int(fs * 0.2)
        p_wave_end = peak
        plt.plot(df['Seg'][p_wave_start:p_wave_end], df['mV'][p_wave_start:p_wave_end], 
                 label='Onda P', color='orange', alpha=0.8)

        # Onda Q
        q_wave_start = peak
        q_wave_end = peak + int(fs * 0.1)
        plt.plot(df['Seg'][q_wave_start:q_wave_end], df['mV'][q_wave_start:q_wave_end], 
                 label='Onda Q', color='blue', alpha=0.8)

        # Onda R
        plt.plot(df['Seg'][peak], df['mV'][peak], "x", label='Onda R', color='red')

        # Onda S
        s_wave_start = peak + int(fs * 0.1)
        s_wave_end = peak + int(fs * 0.3)
        plt.plot(df['Seg'][s_wave_start:s_wave_end], df['mV'][s_wave_start:s_wave_end], 
                 label='Onda S', color='purple', alpha=0.8)

        # Onda T
        t_wave_start = s_wave_end
        t_wave_end = t_wave_start + int(fs * 0.5)
        plt.plot(df['Seg'][t_wave_start:t_wave_end], df['mV'][t_wave_start:t_wave_end], 
                 label='Onda T', color='green', alpha=0.8)

# Configuración de la gráfica
plt.title('Segmentación de las Ondas P, Q, R, S y T en la Señal Original')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('mV')
plt.legend(loc='upper right')
plt.show()
