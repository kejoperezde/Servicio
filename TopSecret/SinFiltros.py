import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Lee el archivo CSV
df = pd.read_csv('TopSecret/Kevin/muestra4.csv')

# Encuentra los picos (R)
peaks, _ = find_peaks(df['mV'], height=0)  # Ajusta el umbral según sea necesario

# Si hay picos, usa el primero como R
if len(peaks) > 0:
    r_index = peaks[0]

    # Definir las posiciones de P, Q, R, S y T
    p_index = r_index - 50  # Ajusta según la señal
    q_index = r_index - 30   # Ajusta según la señal
    s_index = r_index + 30   # Ajusta según la señal
    t_index = r_index + 50   # Ajusta según la señal

    # Asegúrate de que los índices estén dentro de los límites
    indices = [p_index, q_index, r_index, s_index, t_index]
    indices = [i for i in indices if i >= 0 and i < len(df)]

    # Obtiene el valor más alto y más bajo de la columna 'mV'
    max_mv = df['mV'].max()
    min_mv = df['mV'].min()

    # Calcula la media de la columna 'mV'
    mean_mv = df['mV'].mean()

    # Encuentra las posiciones de esos valores
    max_index = df['mV'].idxmax()
    min_index = df['mV'].idxmin()

    seg_max_mv = df['Seg'][max_index]
    seg_min_mv = df['Seg'][min_index]

    # Crea la gráfica
    plt.figure(figsize=(12, 6))
    plt.plot(df['Seg'], df['mV'], linestyle='-', color='b', label='Datos mV')

    # Añade puntos en el valor más alto y más bajo
    plt.scatter(df['Seg'][max_index], max_mv, color='red', label='Máximo mV', s=100, zorder=5)
    plt.scatter(df['Seg'][min_index], min_mv, color='green', label='Mínimo mV', s=100, zorder=5)

    # Añade líneas verticales
    plt.axvline(seg_min_mv, color='green', linestyle='--', label='Línea Mínimo mV')
    plt.axvline(df['Seg'][max_index], color='red', linestyle='--', label='Línea Máximo mV')

    # Añade línea horizontal en la media
    plt.axhline(mean_mv, color='orange', linestyle='--', label='Media mV')

    # Marcar los puntos P, Q, R, S, T
    labels = ['P', 'Q', 'R', 'S', 'T']
    for i, idx in enumerate(indices):
        plt.plot(df['Seg'][idx], df['mV'][idx], 'ro')  # Marcar los puntos
        plt.text(df['Seg'][idx], df['mV'][idx], labels[i], fontsize=12, verticalalignment='bottom', horizontalalignment='right')

    # Personaliza la gráfica
    plt.title('Gráfica de mV vs Seg con Divisiones P, Q, R, S, T')
    plt.xlabel('Seg (s)')
    plt.ylabel('mV')
    plt.grid()
    plt.legend()
    plt.show()
else:
    print("No se encontraron picos en la señal.")
