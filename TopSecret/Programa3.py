import os
import tkinter as tk
import serial
import csv
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog

# Variables glabales
puerto_serie = '/dev/rfcomm0'  # Cambiar puerto
baudrate = 9600
ruta_archivo = './Muestras/muestras.csv'
    
# CENTRAR VENTANA
def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# VENTANA TOMAR MUESTRAS
def tomar_muestras_ventana():
    ventana_cuenta = tk.Toplevel()
    ventana_cuenta.title("Relájate")
    ventana_cuenta.geometry("280x60")
    centrar_ventana(ventana_cuenta, 280, 60)
    
    etiqueta = tk.Label(ventana_cuenta, font=("Helvetica", 14))
    etiqueta.pack(pady=20)

    etiqueta.config(text="Tomando muestra...")
    
    # Inicia la lectura y luego cierra la ventana
    ventana_cuenta.after(1000, lambda: iniciar_lectura_serial(ventana_cuenta, etiqueta))

# FUNCION TOMAR MUESTRAS
def iniciar_lectura_serial(ventana, etiqueta):
    try:
        ser = serial.Serial(puerto_serie, baudrate)
        print(f'Conexión correcta')
        ser.write(b'1')     # write a string, manda al dispositivo que envíe datos

        with open(ruta_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            print('Tomando datos...')
            inicio = time.time()
            escritor_csv.writerow(["Seg", "mV"])  # Escribir encabezados    

            while time.time() - inicio <= 10:  # Dura 10 segundos
                if ser.in_waiting > 0:
                    dato = ser.readline().decode('utf-8').strip()
                    tiempo_transcurrido = time.time() - inicio
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

# SELECCIONAR ARCHIVO
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

# GRAFICAR DATOS
def graficar_datos(seleccionar = False):
    # Leer los datos desde el archivo CSV
    ruta_archivo = seleccionar_archivo() if seleccionar else './Muestras/muestras.csv'
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

# CREAR CARPETA PARA GUARDAR MUESTRAS
if not os.path.exists("Muestras"):
    os.makedirs("Muestras")

# VENTANA PRINCIPAL CONTENEDORA
ventana = tk.Tk()
ventana.title("ECG")
ventana.geometry("300x300")
centrar_ventana(ventana, 300, 300)

# Crear un botón y asignarle la función tomar_muestras_ventana
boton = tk.Button(ventana, text="Tomar muestra", command=tomar_muestras_ventana)
boton.pack(pady=20)

btnGraficar = tk.Button(ventana, text="Mostrar Grafica", command=lambda: graficar_datos(seleccionar=False))
btnGraficar.pack(pady=20)

btnSelectGrafica = tk.Button(ventana, text="Seleccionar CSV", command=lambda: graficar_datos(seleccionar=True))
btnSelectGrafica.pack(pady=20)

btnSalir = tk.Button(ventana, text="Salir", command=ventana.destroy)
btnSalir.pack(pady=20)

# Ejecutar el bucle principal
ventana.mainloop()
