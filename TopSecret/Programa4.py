import tkinter as tk
import serial
import csv
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog

tipo_conexion = None # Variable global para almacenar el tipo de conexión

def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def iniciar_programa(tipo, ventana_seleccion):
    global tipo_conexion
    tipo_conexion = tipo
    
    # Comprobar la conexión
    if not comprobar_conexion(tipo):
        tk.messagebox.showerror("Error de Conexión", "No se pudo establecer la conexión. Verifica el dispositivo.")
        # ventana_seleccion.destroy()  # Cierra la ventana de selección
        return
    
    ventana_seleccion.destroy()  # Cierra la ventana de selección
    crear_ventana_principal()  # Llama a la función para crear la ventana principal.    

def comprobar_conexion(tipo):
    try:
        if tipo == 'usb':
            puerto_serie = '/dev/ttyACM0'  # Cambiar según tu configuración
            # Intenta abrir el puerto para USB
            ser = serial.Serial(puerto_serie, 115200, timeout=1)
            ser.close()  # Cierra el puerto inmediatamente si la conexión es exitosa
        elif tipo == 'bluetooth':
            puerto_serie = '/dev/rfcomm0'  # Cambiar según tu configuración
            # Intenta abrir el puerto para BLUETOOTH
            ser = serial.Serial(puerto_serie, 9600, timeout=1)
            ser.close()  # Cierra el puerto inmediatamente si la conexión es exitosa
        else:
            return False

        return True
    except serial.SerialException:
        return False

# VENTANA
def ventana_seleccion_conexion():
    seleccion = tk.Tk()  # Cambiamos a Tk() para crear una nueva ventana principal temporal
    seleccion.title("Seleccionar Conexión")
    seleccion.geometry("300x150")
    centrar_ventana(seleccion, 300, 150)

    etiqueta = tk.Label(seleccion, text="Tipo de conexión:", font=("Helvetica", 12))
    etiqueta.pack(pady=10)

    btnUSB = tk.Button(seleccion, text="USB", command=lambda: iniciar_programa('usb', seleccion))
    btnUSB.pack(pady=5)

    btnBluetooth = tk.Button(seleccion, text="Bluetooth", command=lambda: iniciar_programa('bluetooth', seleccion))
    btnBluetooth.pack(pady=5)

    seleccion.mainloop()  # Ejecuta el bucle de la ventana de selección

# VENTANA
def crear_ventana_principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Interfaz Gráfica")
    ventana.geometry("300x300")
    centrar_ventana(ventana, 300, 300)

    # Crear botones para la funcionalidad
    boton = tk.Button(ventana, text="Tomar muestra", command=iniciar_cuenta_regresiva)
    boton.pack(pady=20)

    btnGraficar = tk.Button(ventana, text="Mostrar Gráfica", command=lambda: graficar_datos(seleccionar=False))
    btnGraficar.pack(pady=20)

    btnSelectGrafica = tk.Button(ventana, text="Seleccionar CSV", command=lambda: graficar_datos(seleccionar=True))
    btnSelectGrafica.pack(pady=20)

    btnSalir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    btnSalir.pack(pady=20)

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()

def iniciar_cuenta_regresiva():
    ventana_cuenta = tk.Toplevel()
    ventana_cuenta.title("Esperando")
    ventana_cuenta.geometry("280x60")
    centrar_ventana(ventana_cuenta, 280, 60)
    
    etiqueta = tk.Label(ventana_cuenta, font=("Helvetica", 14))
    etiqueta.pack(pady=20)

    etiqueta.config(text="Tomando muestra... ")
    
    ventana_cuenta.after(1000, lambda: iniciar_lectura_serial(ventana_cuenta, etiqueta))

def iniciar_lectura_serial(ventana, etiqueta):
    global tipo_conexion
    if tipo_conexion == 'usb':
        puerto_serie = '/dev/ttyACM0'  # Cambiar puerto según la configuración
        baudrate = 115200
    elif tipo_conexion == 'bluetooth':
        puerto_serie = '/dev/rfcomm0'  # Cambiar puerto según la configuración
        baudrate = 9600
    else:
        etiqueta.config(text="Tipo de conexión no válido.")
        return

    ruta_archivo = '/home/kejoperezde/Documents/Proyecto1/TopSecret/muestras.csv'
    try:
        ser = serial.Serial(puerto_serie, baudrate)
        print(f'Conectado a {puerto_serie} a {baudrate} bps')
        time.sleep(2)  # Esperar a que se establezca la conexión

        with open(ruta_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            print('Esperando datos...')
            inicio = time.time()
            escritor_csv.writerow(["Seg", "mV"])  # Escribir encabezados    

            while time.time() - inicio <= 10.04:  # Dura 10.04 segundos
                if ser.in_waiting > 0:
                    dato = ser.readline().decode('utf-8').strip()
                    tiempo_transcurrido = time.time() - inicio
                    if tiempo_transcurrido > 0.01:
                        escritor_csv.writerow([round(tiempo_transcurrido-0.02, 2), dato])
                        print("Dato guardado")

        print("Toma de muestras finalizada.")
        etiqueta.config(text="Muestras guardadas")
    except serial.SerialException as e:
        etiqueta.config(text="Error de puerto")
    except Exception as e:
        etiqueta.config(text=f"Ocurrió un error: {str(e)}")
    
    ventana.after(1000, ventana.destroy)  # Cierra la ventana después de 1 segundo

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("CSV files", "*.csv")])
    return archivo

def graficar_datos(seleccionar=False):
    ruta_archivo = seleccionar_archivo() if seleccionar else '/home/kejoperezde/Documents/Proyecto1/TopSecret/muestras.csv'
    data = pd.read_csv(ruta_archivo)

    tiempo = data['Seg']
    voltaje = data['mV']

    fig, axs = plt.subplots(3, 1, figsize=(10, 10))

    axs[0].plot(tiempo, voltaje, label='Voltaje (mV)', color='red', marker='')
    axs[0].set_title('Señal Cardiaca')
    axs[0].set_xlabel('Tiempo (s)')
    axs[0].set_ylabel('Voltaje (mV)')
    axs[0].grid()
    
    fourier_transform = np.fft.fft(voltaje)
    frequencies = np.fft.fftfreq(len(voltaje), 0.01)
    
    axs[1].plot(frequencies, np.abs(fourier_transform**2), label='Voltaje (mV)', color='green', marker='')
    axs[1].set_title('Transformada de Fourier (SC)')
    axs[1].set_xlabel('Frecuencia (Hz)')
    axs[1].set_ylabel('Amplitud')
    axs[1].grid()
    
    axs[2].plot(np.fft.fftshift(np.abs(np.fft.fft(voltaje, 256)**2)))
    axs[2].set_title('Transformada de Fourier (Ruido)')
    axs[2].set_xlabel('Frecuencia (Hz)')
    axs[2].set_ylabel('Amplitud')
    axs[2].grid()

    plt.tight_layout()
    plt.show()          

# Iniciar la ventana de selección de conexión al principio
ventana_seleccion_conexion()
