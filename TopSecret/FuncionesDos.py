import os
import serial
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
import pandas as pd
import time
# Filtros
from Filtros.ButterWorth import ButterWorth
from Filtros.PasoAltoyBajo import PasoAltoyBajo
from Filtros.PromedioMovil import PromedioMovil
from Filtros.Wavelet import Wavelet
# Video
import subprocess

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

# RETORNAR SOLO SEÑAL
def get_signal(ruta_archivo):
    dataset = pd.read_csv(ruta_archivo)
    signal = dataset['mV']
    return signal

# GRAFICAR DATOS
def graficar_filtros(ruta_archivo):
    # Leer los datos desde el archivo CSV
    data = pd.read_csv(ruta_archivo)

    # Extraer las columnas
    tiempo = data['Seg']
    voltaje = data['mV']

    # Crear la figura y las subgráficas
    fig, axs = plt.subplots(4, 1, figsize=(10, 10))

    # ButterWorth
    butterWorth = ButterWorth(ruta_archivo)
    # Gráfica
    axs[0].plot(tiempo, butterWorth.aplicar_filtro(), label='Voltaje (mV)', color='red', marker='')
    axs[0].set_title('Butter Worth')
    axs[0].set_xlabel('Tiempo (s)')
    axs[0].set_ylabel('Voltaje (mV)')
    axs[0].grid()
    
    # PasoAltoyBajo
    pasoAltoyBajo = PasoAltoyBajo(ruta_archivo)
    # Gráfica
    axs[1].plot(tiempo, pasoAltoyBajo.aplicar_filtro(), label='Voltaje (mV)', color='red', marker='')
    axs[1].set_title('Paso Alto y Bajo')
    axs[1].set_xlabel('Tiempo (s)')
    axs[1].set_ylabel('Voltaje (mV)')
    axs[1].grid()
    
    # PromedioMovil
    promedioMovil = PromedioMovil(ruta_archivo)
    # Gráfica
    axs[2].plot(tiempo, promedioMovil.aplicar_filtro(), label='Voltaje (mV)', color='red', marker='')
    axs[2].set_title('Promedio Móvil')
    axs[2].set_xlabel('Tiempo (s)')
    axs[2].set_ylabel('Voltaje (mV)')
    axs[2].grid()
    
    # Wavelet
    wavelet = Wavelet(ruta_archivo)
    axs[3].plot(tiempo, wavelet.aplicar_filtro(), label='Voltaje (mV)', color='red', marker='')
    axs[3].set_title('Wavelet')
    axs[3].set_xlabel('Tiempo (s)')
    axs[3].set_ylabel('Voltaje (mV)')
    axs[3].grid()

    # Ajustar el layout
    plt.tight_layout()
    plt.show()  

# GRAFICAR DATOS DE MUESTRA
def graficar_datos(ax, canvas, ruta_archivo):
    ax.clear()
    
    # Etiquetas y título
    ax.set_title("Señal ECG")
    ax.set_ylabel("Amplitud")
    ax.set_xlabel("Segundos")
    
     # Leer los datos desde el archivo CSV
    data = pd.read_csv(ruta_archivo)

    # Extraer las columnas
    tiempo = data['Seg']
    voltaje = data['mV']
    
    # Redibujar la gráfica con el nuevo punto
    ax.plot(tiempo, voltaje, marker='', color='red')
    canvas.draw()  # Redibujar el gráfico

# FUNCION TOMAR MUESTRAS DEL SERIAL
def iniciar_lectura_serial(ventana, etiqueta, archivo_paths, puerto_serie, baudrate, selected_fase):
    
    try:
        ser = serial.Serial(puerto_serie, baudrate)
        print(f'Conexión correcta, tomando datos...')
        ser.write(b'1') # write a string, manda al dispositivo que envíe datos
        
        # CSV de Parte A
        datos = []
        inicio = time.time()
        while time.time() - inicio <= 30:  # Dura 10 segundos
            if ser.in_waiting > 0:
                dato = ser.readline().decode('utf-8').strip()
                tiempo_transcurrido = time.time() - inicio
                datos.append([round(tiempo_transcurrido, 8), int(dato) / 65535.0])  # Almacena en la lista
        # Guardar los datos en el CSV después de recolectarlos
        with open(archivo_paths[0], 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["Seg", "mV"])  # Escribir encabezados
            escritor_csv.writerows(datos)  # Escribir todos los datos de la lista
                            
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
        
    ventana.after(1000, ventana.destroy)
   
# VENTANA TOMAR MUESTRAS
def tomar_muestras(archivo_path, puerto_serie, baudrate, selected_fase):
    ventana_cuenta = tk.Toplevel()
    ventana_cuenta.title("Relájate")
    ventana_cuenta.geometry("280x60")
    centrar_ventana(ventana_cuenta, 280, 60)
    
    etiqueta = tk.Label(ventana_cuenta, font=("Helvetica", 14))
    etiqueta.pack(pady=20)

    etiqueta.config(text="Tomando muestra...")

    # Inicia la lectura y luego cierra la ventana
    # ventana_cuenta.after(1000, iniciar_lectura_serial_arreglo(ventana_cuenta, etiqueta, archivo_path, puerto_serie, baudrate))
    
    iniciar_lectura_serial(ventana_cuenta, etiqueta, archivo_path, puerto_serie, baudrate, selected_fase)
    
# FUNCIÓN PARA OBTENER EL SIGUIENTE NÚMERO DISPONIBLE PARA EL ARCHIVO EN FORMATO _n.csv
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
def crear_carpeta_y_archivo(entry, data, label):
    # Obtener el nombre ingresado en el campo de entrada
    nombre = entry.lower()

    # Crear carpeta si no existe "Muestras"
    carpeta_base = os.path.join(os.getcwd(), "Muestras")
    if not os.path.exists(carpeta_base):
        os.makedirs(carpeta_base)

    # Validar carpeta "Muestras/Nombre"
    carpetas_existentes = [carpeta.lower() for carpeta in os.listdir(carpeta_base) if os.path.isdir(os.path.join(carpeta_base, carpeta))]
    if nombre in carpetas_existentes:
        respuesta = messagebox.askyesno("Advertencia", f"Ya existe una carpeta con el nombre '{nombre}'. ¿Deseas continuar?")
        if not respuesta:
            return
        carpeta_path = os.path.join(carpeta_base, nombre)
        siguiente_numero = obtener_siguiente_numero(carpeta_path, nombre) # Numeracion
    else:
        carpeta_path = os.path.join(carpeta_base, nombre)
        os.makedirs(carpeta_path)
        siguiente_numero = 1 # Numeracion

    # Crear el archivo .csv dentro de la nueva carpeta con el siguiente número
    archivo_path_A = os.path.join(carpeta_path, f"{nombre}-A_{siguiente_numero}.csv")
    with open(archivo_path_A, 'w') as archivo:
        archivo.write("")  # Crear archivo}
        
    # Crear el archivo .csv dentro de la nueva carpeta con el siguiente número
    archivo_path_B = os.path.join(carpeta_path, f"{nombre}-B_{siguiente_numero}.csv")
    with open(archivo_path_B, 'w') as archivo:
        archivo.write("")  # Crear archivo
        
    # Crear el archivo .csv dentro de la nueva carpeta con el siguiente número
    archivo_path_C = os.path.join(carpeta_path, f"{nombre}-C_{siguiente_numero}.csv")
    with open(archivo_path_C, 'w') as archivo:
        archivo.write("")  # Crear archivo
        
    # Crear el archivo .csv dentro de la nueva carpeta con el siguiente número
    archivo_path_D = os.path.join(carpeta_path, f"{nombre}-D_{siguiente_numero}.csv")
    with open(archivo_path_C, 'w') as archivo:
        archivo.write("")  # Crear archivo

    # Actualizar la etiqueta para mostrar el número actual
    label.config(text=f"#{siguiente_numero + 1}")  # Actualizar el texto de la etiqueta
    
    return [archivo_path_A, archivo_path_B, archivo_path_C, archivo_path_D]

def open_video(fase):
    
    fase_map = {
        "1. Baseline": "Videos/Baseline.mp4",
        "2. Stroop": "Videos/StroopColor1.mp4",
        "3. Pausa": "Videos/Pausa.mp4",
        "4. Respiracion": "Videos/Respiracion.mp4"
    }
    
    file_path = fase_map.get(fase, "") 
    
    if file_path and file_path != "":
        try:
            if os.name == "nt":  # Windows
                os.startfile(file_path)
            else:  # macOS y Linux
                subprocess.run(["open" if os.uname().sysname == "Darwin" else "xdg-open", file_path])
        except Exception as e:
            print(f"Error al abrir el video: {e}")
