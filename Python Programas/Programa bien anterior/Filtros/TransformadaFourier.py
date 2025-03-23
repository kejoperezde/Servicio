import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

class FourierTransform:
    
    def __init__(self, ruta_archivo, fs=190):
        """
        Inicializa la clase con la ruta del archivo y la frecuencia de muestreo (190 Hz en este caso).
        - ruta_archivo: Ruta del archivo CSV con los datos.
        - fs: Frecuencia de muestreo de la señal (190 Hz en este caso).
        """
        self.ruta_archivo = ruta_archivo
        self.fs = fs  # Frecuencia de muestreo (190 Hz)
    
    def aplicar_transformada_fourier(self):
        """
        Aplica la transformada de Fourier a la señal ECG y obtiene el espectro de frecuencia.
        """
        # Cargar los datos desde el archivo CSV
        dataset = pd.read_csv(self.ruta_archivo)
        
        # Obtener la señal de la columna 'mV' (suponiendo que el archivo tiene esta columna)
        signal = dataset['mV'].values
        
        # Aplicar la Transformada de Fourier
        N = len(signal)  # Número de muestras (1900)
        fft_signal = np.fft.fft(signal)
        
        # Calcular el espectro de magnitudes (solo la mitad positiva)
        fft_magnitude = np.abs(fft_signal)[:N // 2]
        
        # Calcular las frecuencias correspondientes a cada coeficiente de Fourier
        fft_frequency = np.fft.fftfreq(N, d=1/self.fs)[:N // 2]
        
        return fft_magnitude, fft_frequency

# Uso de la clase
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

ruta_archivo = seleccionar_archivo()
transformada_fourier = FourierTransform(ruta_archivo, fs=190)  # Frecuencia de muestreo 190 Hz
fft_magnitude, fft_frequency = transformada_fourier.aplicar_transformada_fourier()

# Graficar la señal original y su espectro de frecuencia
dataset = pd.read_csv(ruta_archivo)
plt.figure(figsize=(12, 6))

# Graficar señal original
plt.subplot(2, 1, 1)
plt.plot(dataset['Seg'], dataset['mV'], label='Señal Original', color='blue')
plt.title('Señal Original')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('mV')
plt.grid()

# Graficar el espectro de frecuencia
plt.subplot(2, 1, 2)
plt.plot(fft_frequency, fft_magnitude, label='Espectro de Frecuencia', color='orange')
plt.title('Espectro de Frecuencia de la Señal ECG')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid()

plt.tight_layout()
plt.show()
