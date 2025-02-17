# LECTURA HEA Y NORMALIZADO
import scipy.io as sio
import numpy as np

# Extraer info de encabezado (sex and age)
with open('100.hea', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith('#'):
            parts = line.split()
            if len(parts) > 2:
                age = parts[1]  # La edad
                sex = parts[2]  # El género
                break

# Cargar el archivo .mat
data = sio.loadmat('100m.mat')

# Normalizar señal
val = data['val']
normalizado = (val - np.min(val)) / (np.max(val) - np.min(val))

# Agregar nuevas variables al diccionario
data['val'] = normalizado
data['sex'] = sex
data['age'] = age

# Guardar el archivo actualizado
sio.savemat('100m_actualizado.mat', data)
