import numpy as np
import scipy.signal as signal
import scipy.io as sio

# Cargar el archivo .mat
data = sio.loadmat('103m.mat')

# Simple array y normalizado
val = data['val'].squeeze()
ecg_signal = (val - np.min(val)) / (np.max(val) - np.min(val))
sampling_rate = 360  # Frecuencia de muestreo en Hz (360 muestras por segundo)

# Encontrar picos R en la señal
peaks, _ = signal.find_peaks(ecg_signal, height=0.9, distance=sampling_rate*0.6)  # Altura mínima y distancia mínima entre picos

# Calcular intervalos RR en segundos
rr_intervals = np.diff(peaks) / sampling_rate  # Diferencia de índices dividido por la frecuencia de muestreo

# Calcular frecuencia cardíaca (latidos por minuto)
if len(rr_intervals) > 0:
    avg_rr = np.mean(rr_intervals)  # Promedio de los intervalos RR
    heart_rate = 60 / avg_rr  # FC en latidos por minuto
    print(f"Frecuencia Cardíaca: {heart_rate:.2f} lpm")
    aprox = heart_rate * (10/60)
    print(f"Cantidad aprox en 10 seg: {aprox:.2f} lp10seg")
else:
    print("No se detectaron suficientes picos R para calcular la frecuencia cardíaca.")
