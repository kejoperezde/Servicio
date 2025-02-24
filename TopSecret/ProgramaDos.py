import tkinter as tk
from tkinter import ttk
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
centrar_ventana(ventana, 1020, 580)
ventana.configure(bg="#ffffff")
ventana.resizable(False, False)

frame = tk.Frame(ventana, padx=20, pady=10, bg="#ffffff")
frame.pack(pady=10, anchor="center")

labelName = tk.Label(frame, text="Nombre:", bg="#ffffff", font=("Arial", 12))
labelName.grid(row=0, column=0, padx=10, pady=2, sticky="e")
entryName = tk.Entry(frame, width=25, font=("Arial", 12))
entryName.grid(row=0, column=1, padx=10, pady=2, sticky="w")

labelN = tk.Label(frame, text="#1", bg="#ffffff", font=("Arial", 12))
labelN.grid(row=0, column=2, padx=10, pady=2, sticky="w")

labelEdad = tk.Label(frame, text="Edad:", bg="#ffffff", font=("Arial", 12))
labelEdad.grid(row=1, column=0, padx=10, pady=2, sticky="e")
entryEdad = tk.Entry(frame, width=10, font=("Arial", 12))
entryEdad.grid(row=1, column=1, padx=10, pady=2, sticky="w")

labelGenero = tk.Label(frame, text="Género:", bg="#ffffff", font=("Arial", 12))
labelGenero.grid(row=1, column=2, padx=10, pady=2, sticky="e")

genero_var = tk.StringVar()
genero_select = ttk.Combobox(frame, textvariable=genero_var, values=["H", "M"], font=("Arial", 12), width=5, state="readonly")
genero_select.grid(row=1, column=3, padx=10, pady=2, sticky="w")
genero_select.current(0)

buttonFrame = tk.Frame(frame, bg="#ffffff")
buttonFrame.grid(row=2, column=0, columnspan=4, pady=10)

botonMedir = tk.Button(buttonFrame, text="Medir", bg="#4CAF50", fg="white", font=("Arial", 12), width=12, relief=tk.FLAT, command=medir)
botonMedir.pack(side=tk.LEFT, padx=10)

botonSeleccionar = tk.Button(buttonFrame, text="Seleccionar", bg="#FF9800", fg="white", font=("Arial", 12), width=12, relief=tk.FLAT, command=seleccionar)
botonSeleccionar.pack(side=tk.LEFT, padx=10)

fig, ax = plt.subplots(figsize=(10, 4), facecolor='white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 0.08)
ax.set_title("Señal ECG", fontsize=12)
ax.set_ylabel("Amplitud", fontsize=10)
ax.set_xlabel("Segundos", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.6)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(pady=10, anchor="center")

ventana.mainloop()
