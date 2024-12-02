import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# SELECCIONAR ARCHIVO
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

ruta_archivo = seleccionar_archivo()
                                                    
dataset = pd.read_csv(ruta_archivo)

signal = dataset['mV']
tiempo = dataset['Seg']

cutoff_freq = 50  
nyquist_freq = 0.5 * 1000 
order = 4

b, a = butter(order, cutoff_freq/nyquist_freq, btype='low')
# print("The output of the Low band pass Butterworth filter:",b,a)

filtered_signal = filtfilt(b, a, signal)
# print("The output of the filtered Low band pass Butterworth filter:",filtered_signal[:60])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(tiempo, signal)
ax1.set(title='Original signal')

ax2.plot(tiempo, filtered_signal)
ax2.set(title='Filtered signal')

plt.show()