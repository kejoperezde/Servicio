import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
df = pd.read_csv('TopSecret/Kevin/muestra1.csv')

# Obtiene el valor más alto y más bajo de la columna 'mV'
max_mv = df['mV'].max()
min_mv = df['mV'].min()

# Calcula la media de la columna 'mV'
mean_mv = df['mV'].mean()

print(f'La media de mV es: {mean_mv}')

# Encuentra las posiciones de esos valores
max_index = df['mV'].idxmax()
min_index = df['mV'].idxmin()

seg_max_mv = df['Seg'][max_index ]
seg_min_mv = df['Seg'][min_index]

print(f'Valor más alto de mV: {max_mv} , {seg_max_mv}')
print(f'Valor más bajo de mV: {min_mv} , {seg_min_mv}')

# Crea la gráfica
plt.plot(df['Seg'], df['mV'], linestyle='-', color='b', label='Datos mV')

# Añade puntos en el valor más alto y más bajo
plt.scatter(df['Seg'][max_index], max_mv, color='red', label='Máximo mV', s=100, zorder=5)
plt.scatter(df['Seg'][min_index], min_mv, color='green', label='Mínimo mV', s=100, zorder=5)

# Añade líneas verticales
plt.axvline(seg_min_mv, color='green', linestyle='--', label='Línea Mínimo mV')
plt.axvline(df['Seg'][max_index], color='red', linestyle='--', label='Línea Máximo mV')

# Añade línea horizontal en la media
plt.axhline(mean_mv, color='orange', linestyle='--', label='Media mV')

# Personaliza la gráfica
plt.title('Gráfica de mV vs Seg')
plt.xlabel('Seg (s)')
plt.ylabel('mV')
plt.grid()
plt.legend()
plt.show()

import numpy as np

fft=np.fft.fft(np.array(df))
plt.plot(fft)
plt.show()

