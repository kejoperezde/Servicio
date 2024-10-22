import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obtener señal
df = pd.read_csv('TopSecret/Kevin/muestra1.csv')

# Extraer las columnas
tiempo = df['Seg']
voltaje = df['mV']

plt.plot(tiempo, voltaje, label='Voltaje (mV)', color='red', marker='')



plt.show()
