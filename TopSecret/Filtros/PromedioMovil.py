import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# SELECCIONAR ARCHIVO
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

ruta_archivo = seleccionar_archivo()
                                                    
dataset = pd.read_csv(ruta_archivo)

# Definir el tamaño de la ventana del promedio móvil
rango = 6
# Calcular el promedio móvil y agregarlo al dataframe
dataset['promedio_movil'] = dataset['mV'].rolling(window=rango).mean()

# Imprimir las primeras filas del dataframe con el promedio móvil
print(dataset.head(10))

# Extraer las columnas
tiempo = dataset['Seg']
voltaje = dataset['mV']
movil = dataset['promedio_movil']


# Graficar la señal original
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(voltaje)
plt.title('Señal de Frecuencia Cardíaca')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Graficar la transformada de Fourier
plt.subplot(2, 1, 2)
plt.plot(movil)
plt.title('Transformada de Fourier de la Señal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.tight_layout()
plt.show()


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



# Calcular la transformada de Fourier
senal_fft = np.fft.fft(movil)
frecuencias = np.fft.fftfreq(len(movil), d=1/fs)

# Obtener solo la mitad positiva del espectro
idx = np.argsort(frecuencias)
frecuencias = frecuencias[idx]
senal_fft = np.abs(senal_fft[idx])

# Graficar la señal original
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(tiempo, movil)
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