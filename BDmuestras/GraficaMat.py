import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo .mat
data = sio.loadmat('103m.mat')

# Asumiendo que la variable de interés es 'val'
val = data['val'].squeeze()
# Normalizar
normalizado = (val - np.min(val)) / (np.max(val) - np.min(val))

# Crear un eje de tiempo para la gráfica
x = np.arange(len(normalizado))

# Graficar los datos
plt.figure(figsize=(10, 5))
plt.plot(x, normalizado, label='Señal normalizada del archivo 100m.mat', color='b')
plt.xlabel('Muestras')
plt.ylabel('Amplitud normalizada')
plt.title('Visualización de datos normalizados desde 100m.mat')
plt.legend()
plt.grid()
plt.show()
