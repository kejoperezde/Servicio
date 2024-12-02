import os
import serial
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import csv
import pandas as pd
import time

# Variables glabales
puerto_serie = '/dev/rfcomm0'  # Cambiar puerto
baudrate = 9600
    
# CENTRAR VENTANA
def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# SELECCIONAR ARCHIVO
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

# GRAFICAR DATOS
def graficar_datos():
    # Leer los datos desde el archivo CSV
    ruta_archivo = seleccionar_archivo()
    data = pd.read_csv(ruta_archivo)

    # Extraer las columnas
    tiempo = data['Seg']
    voltaje = data['mV']

    # Crear la figura y las subgráficas
    fig, axs = plt.subplots(3, 1, figsize=(10, 10))

    # Gráfica señal cardiaca
    axs[0].plot(tiempo, voltaje, label='Voltaje (mV)', color='red', marker='')
    axs[0].set_title('Señal Cardiaca')
    axs[0].set_xlabel('Tiempo (s)')
    axs[0].set_ylabel('Voltaje (mV)')
    axs[0].grid()
    
    fourier_transform = np.fft.fft(voltaje)
    frequencies = np.fft.fftfreq(len(voltaje),0.01)
    
    # Gráfica transformada de Fourier con la seña cardiaca
    axs[1].plot(frequencies, np.abs(fourier_transform/np.max(fourier_transform)**2), label='Voltaje (mV)', color='green', marker='')
    # axs[1].stem(np.fft.fftshift(np.fft.fft(voltaje,256)))
    axs[1].set_title('Transformada de Fourier (SC)')
    axs[1].set_xlabel('Tiempo (s)')
    axs[1].set_ylabel('Voltaje (mV)')
    axs[1].grid()
    
    # Gráfica del ruido
    #axs[2].plot(tiempo, voltaje, label='Voltaje con Ruido (mV)', color='blue', marker='')
    axs[2].plot(np.fft.fftshift(np.abs(np.fft.fft(voltaje,256))))
    axs[2].set_title('Transformada de Fourier (Ruido)')
    axs[2].set_xlabel('Tiempo (s)')
    axs[2].set_ylabel('Voltaje (mV)')
    axs[2].grid()

    # Ajustar el layout
    plt.tight_layout()
    plt.show()          

# FUNCION TOMAR MUESTRAS
def iniciar_lectura_serial(ventana, etiqueta, archivo_path):
    try:
        ser = serial.Serial(puerto_serie, baudrate)
        print(f'Conexión correcta')
        ser.write(b'1')     # write a string, manda al dispositivo que envíe datos

        with open(archivo_path, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            print('Tomando datos...')
            inicio = time.time()
            escritor_csv.writerow(["Seg", "mV"])  # Escribir encabezados    

            while time.time() - inicio <= 10:  # Dura 10 segundos
                if ser.in_waiting > 0:
                    dato = ser.readline().decode('utf-8').strip()
                    tiempo_transcurrido = time.time() - inicio
                    #escritor_csv.writerow([0, int(dato) / 65535.0]) # Normaliza el valor a [0, 1]
                    escritor_csv.writerow([round(tiempo_transcurrido, 5), int(dato) / 65535.0]) # Normaliza el valor a [0, 1]
                    # print("Dato guardado")

        print("Toma de muestras finalizada.")
        etiqueta.config(text="Muestras guardadas")
    except serial.SerialException as e:
        etiqueta.config(text=f"Error de conexión")
        print(f"Error: {str(e)}")
    except Exception as e:
        etiqueta.config(text=f"Ocurrió un error")
        print(f"Error: {str(e)}")
    finally:
        ser.write(b'0')     # write a string, manda al dispositivo para que deje de enviar datos
        ser.close()
    
    ventana.after(1000, ventana.destroy)  # Cierra la ventana después de 1 segundo

# VENTANA TOMAR MUESTRAS
def tomar_muestras_ventana(archivo_path):
    ventana_cuenta = tk.Toplevel()
    ventana_cuenta.title("Relájate")
    ventana_cuenta.geometry("280x60")
    centrar_ventana(ventana_cuenta, 280, 60)
    
    etiqueta = tk.Label(ventana_cuenta, font=("Helvetica", 14))
    etiqueta.pack(pady=20)

    etiqueta.config(text="Tomando muestra...")
    
    # Inicia la lectura y luego cierra la ventana
    ventana_cuenta.after(1000, lambda: iniciar_lectura_serial(ventana_cuenta, etiqueta, archivo_path))

# Función para obtener el siguiente número disponible para el archivo en formato _n.txt
def obtener_siguiente_numero(carpeta_path, nombre):
    # Listar todos los archivos dentro de la carpeta
    archivos = os.listdir(carpeta_path)
    
    # Filtrar los archivos que sigan el patrón de nombre_n.txt
    archivos_filtrados = [archivo for archivo in archivos if archivo.startswith(f"{nombre}_") and archivo.endswith(".csv")]
    
    # Obtener los números existentes en los archivos (por ejemplo, 1, 2, 3, ...)
    numeros_existentes = []
    for archivo in archivos_filtrados:
        try:
            # Extraer el número del archivo (por ejemplo, de "nombre_1.txt" extraemos "1")
            numero = int(archivo.split('_')[1].split('.')[0])
            numeros_existentes.append(numero)
        except ValueError:
            continue  # Si no se puede convertir a número, lo ignoramos
    
    # Si hay archivos con números, obtenemos el siguiente número (máximo + 1)
    siguiente_numero = max(numeros_existentes, default=0) + 1
    
    return siguiente_numero

# Función para crear carpeta y archivo
def crear_carpeta_y_archivo():
    if not entryName.get().strip():  # Verifica si el campo está vacío
        messagebox.showwarning("Advertencia", "Ponle un nombre a la muestra")
        return  # No hace nada si está vacío
    
    # Obtener el nombre ingresado en el campo de entrada
    nombre = entryName.get().lower()

    # Convertir el nombre a minúsculas para verificar si ya existe una carpeta con el mismo nombre
    nombre_normalizado = nombre

    # Ruta de la carpeta "Muestras"
    carpeta_base = os.path.join(os.getcwd(), "Muestras")

    # Verificar si la carpeta "Muestras" existe
    if not os.path.exists(carpeta_base):
        # Si no existe, la creamos
        os.makedirs(carpeta_base)

    # Obtener lista de carpetas en "Muestras"
    carpetas_existentes = [carpeta.lower() for carpeta in os.listdir(carpeta_base) if os.path.isdir(os.path.join(carpeta_base, carpeta))]

    # Verificar si ya existe una carpeta con el mismo nombre (sin importar mayúsculas/minúsculas)
    if nombre_normalizado in carpetas_existentes:
        # Mostrar una ventana de confirmación con opciones de "Continuar" o "Cancelar"
        respuesta = messagebox.askyesno("Advertencia", f"Ya existe una carpeta con el nombre '{nombre}'. ¿Deseas continuar?")
        
        # Si el usuario elige "Cancelar" (No)
        if not respuesta:
            return  # No continuar si elige "Cancelar"
        
        # Si elige "Continuar", verificamos el siguiente número disponible
        carpeta_path = os.path.join(carpeta_base, nombre)
        siguiente_numero = obtener_siguiente_numero(carpeta_path, nombre)
    else:
        # Si la carpeta no existe, creamos una nueva y empezamos desde el número 2
        carpeta_path = os.path.join(carpeta_base, nombre)
        os.makedirs(carpeta_path)
        siguiente_numero = 1

    # Crear el archivo .txt dentro de la nueva carpeta con el siguiente número
    archivo_path = os.path.join(carpeta_path, f"{nombre}_{siguiente_numero}.csv")
    with open(archivo_path, 'w') as archivo:
        archivo.write("")  # Escribir el nombre y el número en el archivo
        # archivo.write(f"{nombre}_{siguiente_numero}")  # Escribir el nombre y el número en el archivo

    tomar_muestras_ventana(archivo_path)

    # Actualizar la etiqueta para mostrar el número actual
    labelN.config(text=f"#{siguiente_numero + 1}")  # Actualizar el texto de la etiqueta

def graficar_punto(x, y):
    # Agregar el punto a los valores
    x_vals.append(x)
    y_vals.append(y)

    # Redibujar la gráfica con el nuevo punto
    ax.plot(x_vals, y_vals, marker='o', color='b')
    canvas.draw()  # Redibujar el gráfico

# VENTANA PRINCIPAL CONTENEDORA
ventana = tk.Tk()
ventana.title("Programa ECG")

# Centrar la ventana en la pantalla
ancho_ventana = 1020  # Ancho deseado de la ventana
alto_ventana = 490   # Alto deseado de la ventana

# Obtener las dimensiones de la pantalla
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana
posicion_x = (pantalla_ancho // 2) - (ancho_ventana // 2)
posicion_y = (pantalla_alto // 2) - (alto_ventana // 2)

# Establecer la geometría de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

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
botonMedir = tk.Button(ventana, text="Medir", bg="green", fg="white", command=crear_carpeta_y_archivo)
botonMedir.grid(row=0, column=3, padx=10, pady=20)

# Botón en la fila 1, columna 0
botonSeleccionar = tk.Button(ventana, text="Seleccionar", bg="orange", fg="white", command=graficar_datos)
botonSeleccionar.grid(row=0, column=4, padx=10, pady=20)

# /**********************************************/ #
# Crear la figura de Matplotlib con fondo blanco
fig, ax = plt.subplots(figsize=(10, 4), facecolor='white')  # Fondo blanco

# Establecer límites para los ejes
ax.set_xlim(0, 10)  # Eje x de 0 a 10
ax.set_ylim(0, 0.8)  # Eje y de 0 a 0.8

# Inicializar el gráfico
x_vals = []
y_vals = []

# Etiquetas y título
ax.set_title("Señal ECG")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")

# Integrar la figura con Tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)  # Ventana es el contenedor principal
canvas.draw()
canvas.get_tk_widget().grid(row=1, columnspan=5, padx=10, pady=10)
# /**********************************************/ #

# Ejecutar el bucle principal
ventana.mainloop()