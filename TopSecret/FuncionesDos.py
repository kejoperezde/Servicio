import os
import serial
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import csv
import pandas as pd
import time
import subprocess
from Filtros.ButterWorthN import ButterWorthN


### ===========================  FUNCIONES DE INTERFAZ GRÁFICA  =========================== ###

def centrar_ventana(ventana, ancho, alto):
    """Centrar ventana en la pantalla."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def seleccionar_archivo():
    """Abrir un cuadro de diálogo para seleccionar un archivo CSV."""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

### ===========================  FUNCIONES PARA MANEJO DE ARCHIVOS  =========================== ###

def crear_carpeta_y_archivo(nombre, fase):
    """
    Crea una carpeta dentro de 'Muestras' con el nombre del usuario y 
    un archivo CSV único basado en la fase seleccionada.

    Parámetros:
    - nombre (str): Nombre del usuario (subcarpeta).
    - fase (str): Fase seleccionada.

    Retorna:
    - str: Ruta del archivo CSV creado o None si se cancela.
    """

    # Mapeo de fases a nombres de archivos
    fase_map = {
        "0. Prueba": "N",
        "1. Baseline": "A",
        "2. Stroop": "B",
        "3. Pausa": "C",
        "4. Respiracion": "D"
    }

    # Normalizar nombre
    nombreLow = nombre.lower().strip()
    carpeta_base = os.path.join(os.getcwd(), "Muestras")

    # Crear carpeta base si no existe
    if not os.path.exists(carpeta_base):
        os.makedirs(carpeta_base)

    # Ruta de la subcarpeta del usuario
    carpeta_path = os.path.join(carpeta_base, nombreLow)

    # Crear subcarpeta si no existe
    if not os.path.exists(carpeta_path):
        os.makedirs(carpeta_path)
    else:
        respuesta = messagebox.askyesno("Advertencia", f"La carpeta '{nombreLow}' ya existe. ¿Deseas continuar?")
        if not respuesta:
            return None  # Cancelar la operación

    # Obtener nombre base del archivo basado en la fase
    nombre_fase = fase_map.get(fase)

    # Buscar archivos existentes con la misma fase
    archivos_existentes = [archivo for archivo in os.listdir(carpeta_path) if archivo.startswith(f"{nombreLow}_{nombre_fase}") and archivo.endswith(".csv")]
    numeros_existentes = []

    for archivo in archivos_existentes:
        try:
            numero = int(archivo.split('_')[-1].split('.')[0])  # Extraer el número final
            numeros_existentes.append(numero)
        except (IndexError, ValueError):
            continue

    # Determinar el siguiente número disponible
    siguiente_numero = max(numeros_existentes, default=0) + 1
    archivo_csv = f"{nombreLow}_{nombre_fase}_{siguiente_numero}.csv"
    archivo_path = os.path.join(carpeta_path, archivo_csv)

    # Crear el archivo CSV con encabezados
    with open(archivo_path, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Seg", "mV"])  # Encabezados del CSV

    print(f"Archivo creado: {archivo_path}")
    return archivo_path


### ===========================  FUNCIONES PARA PROCESAMIENTO DE DATOS  =========================== ###

def graficar_datos(ax, canvas, ruta_archivo):
    """Graficar los datos de un archivo CSV."""
    ax.clear()
    ax.set_title("Señal ECG Filtro ButterWorth")
    ax.set_ylabel("Amplitud")
    ax.set_xlabel("Segundos")

    # Cargar datos del archivo CSV
    data = pd.read_csv(ruta_archivo)

    # Crear instancia del filtro Butterworth
    filtro = ButterWorthN(fs=192)  # Asegúrate de usar la misma frecuencia de muestreo

    # Aplicar filtro a la columna de mV
    señal_filtrada = filtro.apply_filter(data['mV'])

    # Graficar la señal filtrada
    ax.plot(data['Seg'], señal_filtrada, marker='', color='red', label="ECG Filtrado")  
    ax.legend()

    # Redibujar el canvas de Tkinter
    canvas.draw()

import serial
import csv
import time
import tkinter as tk
from tkinter import messagebox

def iniciar_lectura_serial(archivo_path, puerto_serie, baudrate, selected_fase):
    """
    Inicia la lectura del puerto serial y guarda los datos en un archivo CSV.
    """
    
    # Duraciones según la fase seleccionada
    duracion_map = {
        "0. Prueba": 10,
        "1. Baseline": 180,
        "2. Stroop": 180,
        "3. Pausa": 60,
        "4. Respiracion": 180
    }
    duracion = duracion_map.get(selected_fase, 30)  # Valor por defecto de 30 segundos si la fase no se encuentra

    # Crear ventana de Tkinter oculta para mostrar los alertas sin una interfaz gráfica visible
    root = tk.Tk()
    root.withdraw()

    try:
        ser = serial.Serial(puerto_serie, baudrate)

        ser.write(b'1')  # Inicia la transmisión de datos desde el dispositivo

        inicio = time.time()
        
        with open(archivo_path, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            print('Tomando datos...')
            inicio = time.time()
            escritor_csv.writerow(["Seg", "mV"])  # Escribir encabezados    

            while time.time() - inicio <= duracion:  # Dura 10 segundos
                if ser.in_waiting > 0:
                    dato = ser.readline().decode('utf-8').strip()
                    tiempo_transcurrido = time.time() - inicio
                    escritor_csv.writerow([round(tiempo_transcurrido, 8), int(dato) / 65535.0]) # Normaliza el valor a [0, 1]

        mensaje_fin = f"Toma de muestras finalizada para la fase '{selected_fase}'."
        messagebox.showinfo("Fin de Toma de Muestras", mensaje_fin)

    except serial.SerialException as e:
        messagebox.showerror("Error de Conexión", f"No se pudo abrir el puerto serial.\nError: {str(e)}")
        print(f"Error de conexión serial: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado.\nError: {str(e)}")
        print(f"Error inesperado: {str(e)}")
    finally:
        if 'ser' in locals() and ser.is_open:
            try:
                ser.write(b'0')  # Detener la transmisión de datos
                ser.close()
                print("Conexión serial cerrada.")
            except Exception:
                pass

### ===========================  FUNCIÓN PARA REPRODUCIR VIDEO  =========================== ###

def open_video(fase):
    """Abrir un video según la fase seleccionada."""
    fase_map = {
        "1. Baseline": "Videos/Baseline.mp4",
        "2. Stroop": "Videos/StroopColor1.mp4",
        "3. Pausa": "Videos/Pausa.mp4",
        "4. Respiracion": "Videos/Respiracion.mp4"
    }

    file_path = fase_map.get(fase)
    
    if file_path:
        try:
            if os.name == "nt":  # Windows
                os.startfile(file_path)
            else:  # macOS y Linux
                subprocess.run(["open" if os.uname().sysname == "Darwin" else "xdg-open", file_path])
        except Exception as e:
            print(f"Error al abrir el video: {e}")

