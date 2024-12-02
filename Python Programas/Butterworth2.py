# import required modules 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 
import math 

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

ss = dataset['mV']
tiempo = dataset['Seg']

# Specifications of Filter 

# sampling frequency 
f_sample = 40000

# pass band frequency 
f_pass = 4000

# stop band frequency 
f_stop = 8000

# pass band ripple 
fs = 0.5

# pass band freq in radian 
wp = f_pass/(f_sample/2) 

# stop band freq in radian 
ws = f_stop/(f_sample/2) 

# Sampling Time 
Td = 1

# pass band ripple 
g_pass = 0.5

# stop band attenuation 
g_stop = 40


# Conversion to prewrapped analog frequency 
omega_p = (2/Td)*np.tan(wp/2) 
omega_s = (2/Td)*np.tan(ws/2) 


# Design of Filter using signal.buttord function 
N, Wn = signal.buttord(omega_p, omega_s, g_pass, g_stop, analog=True) 


# Printing the values of order & cut-off frequency! 
print("Order of the Filter=", N) # N is the order 
# Wn is the cut-off freq of the filter 
print("Cut-off frequency= {:.3f} rad/s ".format(Wn)) 


# Conversion in Z-domain 

# b is the numerator of the filter & a is the denominator 
b, a = signal.butter(N, Wn, 'low', True) 
z, p = signal.bilinear(b, a, fs) 
# w is the freq in z-domain & h is the magnitude in z-domain 
w, h = signal.freqz(z, p, 512) 


# Magnitude Response 
plt.semilogx(w, 20*np.log10(abs(h))) 
plt.xscale('log') 
plt.title('Butterworth filter frequency response') 
plt.xlabel('Frequency [Hz]') 
plt.ylabel('Amplitude [dB]') 
plt.margins(0, 0.1) 
plt.grid(which='both', axis='both') 
plt.axvline(100, color='green') 


# Impulse Response 
imp = signal.unit_impulse(40) 
c, d = signal.butter(N, 0.5) 

response = signal.lfilter(c, d, imp) 
plt.stem(np.arange(0, 40), imp) 
plt.stem(np.arange(0, 40), response) 
plt.margins(0, 0.1) 
plt.xlabel('Time [samples]') 
plt.ylabel('Amplitude') 
plt.grid(True) 


# Phase Response 
fig, ax1 = plt.subplots() 
ax1.set_title('Digital filter frequency response') 
ax1.set_ylabel('Angle(radians)', color='g') 
ax1.set_xlabel('Frequency [Hz]') 
angles = np.unwrap(np.angle(h)) 
ax1.plot(w/2*np.pi, angles, 'g') 
ax1.grid() 
ax1.axis('tight') 

### APLICAR EL FILTRO

filtered_signal = signal.filtfilt(b, a, ss)
print("The output of the filtered Low band pass Butterworth filter:",filtered_signal[:60])

fig, (ax2, ax3) = plt.subplots(2, 1, sharex=True)

ax2.plot(tiempo, ss)
ax2.set(title='Original signal')

ax3.plot(tiempo, filtered_signal)
ax3.set(title='Filtered signal')

plt.show()