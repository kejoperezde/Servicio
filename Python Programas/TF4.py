import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from scipy.fft import fft, rfft
from scipy.fft import fftfreq, rfftfreq

# SELECCIONAR ARCHIVO
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

ruta_archivo = seleccionar_archivo()

# Obtener señal
df = pd.read_csv(ruta_archivo)

# Extraer las columnas
voltaje = df['mV']
tiempo = df['Seg']

# umpy arrays
tiempo = np.array(tiempo)
voltaje = np.array(voltaje)

# Frecuencia de muestreo, calcula la frecuencia de muestreo a partir del tiempo
fs = 1 / np.mean(np.diff(tiempo))

# Calcular la transformada de Fourier
senal_fft = np.fft.fft(voltaje)
frecuencias = np.fft.fftfreq(len(voltaje), d=1/fs)

# Obtener solo la mitad positiva del espectro
idx = np.argsort(frecuencias)
frecuencias = frecuencias[idx]
senal_fft = np.abs(senal_fft[idx])


# Apply the FFT on the signal
fourier = fft(voltaje)


# Calculate N/2 to normalize the FFT output
N = len(voltaje)
normalize = N/2


# Get the frequency components of the spectrum
sampling_rate = 180.0 # It's used as a sample spacing
frequency_axis = fftfreq(N, d=1.0/sampling_rate)
norm_amplitude = np.abs(fourier)/normalize
# Plot the results



# Graficar la señal original
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(tiempo, voltaje)
plt.title('Señal de Frecuencia Cardíaca')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Graficar la transformada de Fourier
plt.subplot(2, 1, 2)
# plt.plot(frecuencias[:len(frecuencias)//2], senal_fft[:len(senal_fft)//2])
# Plot the result (the spectrum |Xk|)
# plt.plot(np.abs(fourier))

# Plot the normalized FFT (|Xk|)/(N/2)
# plt.plot(np.abs(fourier)/normalize)

# Get the frequency components of the spectrum
plt.plot(frequency_axis, norm_amplitude)

plt.title('Transformada de Fourier de la Señal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')

plt.tight_layout()
plt.show()
