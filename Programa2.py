import tkinter as tk
import random
import matplotlib.pyplot as plt
import csv
from time import sleep
from machine import ADC

adc = ADC(26)

def tomar_muestra():
    while True:
        medicion = adc.read_u16() / 2**16
        resultado.set(f"Números generados: {medicion}")
        sleep(0.05)

def salir():
    ventana.destroy()  # Cierra la ventana y termina el programa

def leer_datos_csv(ruta):
    datos = []
    try:
        with open(ruta, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if fila:  # Asegurarse de que la fila no esté vacía
                    datos.append(int(fila[0]))  # Convertir a entero
    except FileNotFoundError:
        resultado.set("Error: Archivo no encontrado.")
    return datos

def mostrar_graficas():
    # Leer datos de un archivo CSV
    datos1 = leer_datos_csv('datos1.csv')  # Cambia esto a la ruta de tu archivo CSV
    datos2 = leer_datos_csv('datos2.csv')  # Cambia esto a la ruta de tu archivo CSV

    # Crear la primera gráfica
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, 1ª gráfica
    plt.bar(range(len(datos1)), datos1, color='blue')
    plt.title("Gráfica 1")
    plt.xlabel("Índice")
    plt.ylabel("Valor")

    # Crear la segunda gráfica
    plt.subplot(1, 2, 2)  # 1 fila, 2 columnas, 2ª gráfica
    plt.plot(datos2, color='red', marker='o')
    plt.title("Gráfica 2")
    plt.xlabel("Índice")
    plt.ylabel("Valor")

    # Mostrar las gráficas
    plt.tight_layout()
    plt.show()  # Esto abrirá la ventana de Matplotlib

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Números Aleatorios")
ventana.geometry("400x200")  # Establecer dimensiones (ancho x alto)

# Crear una variable para mostrar el resultado
resultado = tk.StringVar()

# Crear un botón para generar números
boton_generar = tk.Button(ventana, text="Generar Números", command=tomar_muestra)
boton_generar.pack(pady=10)

# Crear un botón para abrir las gráficas
boton_graficas = tk.Button(ventana, text="Mostrar Gráficas", command=mostrar_graficas)
boton_graficas.pack(pady=10)

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
