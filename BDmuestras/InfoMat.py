import scipy.io as sio
import numpy as np

# Cargar el archivo .mat
data = sio.loadmat('103m.mat')
# data = sio.loadmat('100m.mat')

# direct_keys
print(data.keys())

# Señal original
val = data['val'].squeeze()
print(val)

# Normalizar señal
normalizado = (val - np.min(val)) / (np.max(val) - np.min(val))
print(normalizado)
