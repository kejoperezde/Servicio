import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

numeracion = [
    100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 
    117, 118, 119, 121, 122, 123, 124, 200, 201, 202, 203, 205, 207, 208, 209, 210, 
    212, 213, 214, 215, 217, 219, 220, 221, 222, 223, 228, 230, 231, 232, 233, 234
]

# Cargar el archivo .mat
data = sio.loadmat('datos_ecg/datos_101.mat')

# Info
print(data.keys())
print(data)
print(data['diseases'])
print(data['lpdiezseg'])

# Asumiendo que la variable de interés es 'val'
val = data['normalizado'].squeeze()

# Crear un eje de tiempo para la gráfica
x = np.arange(len(val))

# Graficar los datos
plt.figure(figsize=(10, 5))
plt.plot(x, val, label='Señal normalizada del archivo 100m.mat', color='b')
plt.xlabel('Muestras')
plt.ylabel('Amplitud normalizada')
plt.title('Visualización de datos normalizados desde 100m.mat')
plt.legend()
plt.grid()
plt.show()

secciones = data['secciones'][0] if len(data['secciones']) == 1 else data['secciones']

num_secciones = len(secciones)

# Crear una figura con subgráficos
fig, axes = plt.subplots(num_secciones, 1, figsize=(10, 2 * num_secciones), sharex=True)

# Graficar cada sección
for i, seccion in enumerate(secciones):
    if isinstance(seccion, np.ndarray):
        seccion = seccion.flatten()  # Asegurarse de que sea un array unidimensional

    x = np.arange(len(seccion))  # Eje x (índices de las muestras)
    axes[i].plot(x, seccion, label=f'Sección {i+1}', color='b')
    axes[i].legend()
    axes[i].grid()

plt.xlabel('Muestras')
plt.suptitle('Visualización de datos normalizados')
plt.tight_layout()
plt.show()