import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

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
tiempo = df['Seg']
voltaje = df['mV']

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

# Graficar la señal original
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(tiempo, voltaje)
plt.title('Señal de Frecuencia Cardíaca')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Graficar la transformada de Fourier
plt.subplot(2, 1, 2)
plt.plot(frecuencias[:len(frecuencias)//2]*-1, senal_fft[:len(senal_fft)//2]-1)
plt.title('Transformada de Fourier de la Señal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.tight_layout()
plt.show()
