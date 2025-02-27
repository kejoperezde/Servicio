import os
import tkinter as tk
from tkinter import messagebox

def crear_carpeta(nombre):
    nombreLow = nombre.lower()
    # Crear carpeta Muestras si no existe
    carpeta_base = os.path.join(os.getcwd(), "Muestras")
    if not os.path.exists(carpeta_base):
        os.makedirs(carpeta_base)
    # Crear carpteta del nombre
    if os.path.exists(carpeta_base + "/" + nombreLow):
        respuesta = messagebox.askyesno("Carpeta existente", f"La carpeta '{nombreLow}' ya existe. ¿Desea continuar?")
        if not respuesta:
            return
    else:
        os.makedirs(nombreLow)
        print(f"Carpeta creada: {nombreLow}")
    
    print(f"Operación completada en la carpeta: {nombreLow}")
    
crear_carpeta("kevin")