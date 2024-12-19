import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tkinter as tk
from tkinter import filedialog

# Función para seleccionar el archivo
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

# Leer el archivo CSV
datos = pd.read_csv(seleccionar_archivo())

# Usar solo la columna "mV"
df = pd.DataFrame(datos, columns=["Seg", "mV"])

mV_scaled = df[["mV"]]

# Convertir la columna "mV" a tensores de PyTorch
entradas = torch.tensor(mV_scaled[:-1700].to_numpy(), dtype=torch.float32)  # Señales de ECG (mV), sin la última fila
salidas = torch.tensor(mV_scaled[1700:].to_numpy(), dtype=torch.float32)   # Señales de ECG (mV), desplazadas 1 paso

# Verificar si CUDA está disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Usando dispositivo: {device}")

# Mover los datos al dispositivo (GPU o CPU)
entradas = entradas.to(device)
salidas = salidas.to(device)

# Definir la arquitectura de la red neuronal
class RedNeuronal(nn.Module):
    def __init__(self):
        super(RedNeuronal, self).__init__()
        self.capa_oculta = nn.Linear(1, 500)  # Capa oculta con 5 neuronas
        self.capa_salida = nn.Linear(500, 1)  # Capa de salida con 1 neurona
    
    def forward(self, x):
        x = torch.tanh(self.capa_oculta(x))  # Activación ReLU
        x = self.capa_salida(x)
        return x

# Crear una instancia del modelo y moverlo al dispositivo
modelo = RedNeuronal().to(device)

# Definir la función de pérdida y el optimizador
criterio = nn.L1Loss()  # Error cuadrático medio
optimizador = optim.Adam(modelo.parameters(), lr=1e-2)

# Entrenamiento de la red neuronal
num_epochs = 100000
for epoch in range(num_epochs):
    # Paso hacia adelante
    predicciones = modelo(entradas.view(-1, 1))  # Redimensionar la entrada
    
    # Calcular la pérdida
    loss = criterio(predicciones, salidas.view(-1, 1))  # Redimensionar las salidas
    
    # Paso hacia atrás
    optimizador.zero_grad()  # Borrar gradientes anteriores
    loss.backward()  # Retropropagación
    
    # Actualizar los parámetros
    optimizador.step()
    
    # Mostrar el progreso del entrenamiento
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Pérdida: {loss.item():.4f}')

# Después del entrenamiento, mostrar las predicciones finales
with torch.no_grad():
    predicciones_finales = modelo(entradas.view(-1, 1))
    predicciones_finales_cpu = predicciones_finales.cpu().numpy()
    print("Predicciones finales: ", predicciones_finales_cpu)

    # Desnormalizar las predicciones para verlas en la escala original
    predicciones_finales_originales = scaler.inverse_transform(
        np.hstack((entradas.cpu().numpy(), predicciones_finales_cpu))
    )
    print("Predicciones desnormalizadas: ", predicciones_finales_originales[:, 1])
