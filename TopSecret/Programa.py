import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Archivos
from Funciones import *

# Variables glabales
puerto_serie = '/dev/rfcomm0'  # Cambiar puerto
baudrate = 9600 

def medir():
    archivo_path = crear_carpeta_y_archivo(entryName, labelN)
    if archivo_path != None:
        tomar_muestras(archivo_path, puerto_serie, baudrate)
        graficar_datos(ax, canvas, archivo_path)
    
def seleccionar():  
    archivo_path = seleccionar_archivo()
    if archivo_path:
        # graficar_datos(ax, canvas, archivo_path)
        graficar_filtros(archivo_path)
    
# VENTANA PRINCIPAL CONTENEDORA
ventana = tk.Tk()
ventana.title("Programa ECG")
centrar_ventana(ventana, 1020, 490)

# Etiqueta en la fila 0, columna 0
labelName = tk.Label(ventana, text="Nombre:")
labelName.grid(row=0, column=0, padx=10, pady=10)

# Entrada de texto en la fila 0, columna 1
entryName = tk.Entry(ventana)
entryName.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta en la fila 0, columna 0
labelN = tk.Label(ventana, text="#1")
labelN.grid(row=0, column=2, padx=10, pady=10)

# Botón en la fila 1, columna 0
botonMedir = tk.Button(ventana, text="Medir", bg="green", fg="white", command= lambda: medir())
botonMedir.grid(row=0, column=3, padx=10, pady=20)

# Botón en la fila 1, columna 0
botonSeleccionar = tk.Button(ventana, text="Seleccionar", bg="orange", fg="white", command=seleccionar)
botonSeleccionar.grid(row=0, column=4, padx=10, pady=20)

# /**********************************************/ #
# Crear la figura de Matplotlib con fondo blanco
fig, ax = plt.subplots(figsize=(10, 4), facecolor='white')  # Fondo blanco

# Establecer límites para los ejes
ax.set_xlim(0, 10)  # Eje x de 0 a 10
ax.set_ylim(0, 0.08)  # Eje y de 0 a 0.8

# Etiquetas y título
ax.set_title("Señal ECG")
ax.set_ylabel("Amplitud")
ax.set_xlabel("Segundos")

# Integrar la figura con Tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)  # Ventana es el contenedor principal
canvas.draw()
canvas.get_tk_widget().grid(row=1, columnspan=5, padx=10, pady=10)
# /**********************************************/ #

# Ejecutar el bucle principal
ventana.mainloop()