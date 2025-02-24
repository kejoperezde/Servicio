import serial
import scipy.io as sio
import numpy as np
import tkinter as tk
from tkinter import ttk
from threading import Thread

class SerialReader:
    def __init__(self, ventana, archivo_path, puerto_serie, baudrate):
        self.ventana = ventana
        self.archivo_path = archivo_path
        self.puerto_serie = puerto_serie
        self.baudrate = baudrate
        self.ser = None
        self.valores = []
        self.leyendo = False
        
        frame = tk.Frame(self.ventana, bg="#FFFFFF")
        frame.pack(padx=10, pady=10)

        self.labelName = tk.Label(frame, text="Nombre:", bg="#FFFFFF", font=("Arial", 12))
        self.labelName.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entryName = tk.Entry(frame, width=25, font=("Arial", 12))
        self.entryName.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.labelN = tk.Label(frame, text="#1", bg="#FFFFFF", font=("Arial", 12))
        self.labelN.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.labelEdad = tk.Label(frame, text="Edad:", bg="#FFFFFF", font=("Arial", 12))
        self.labelEdad.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entryEdad = tk.Entry(frame, width=10, font=("Arial", 12))
        self.entryEdad.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.labelGenero = tk.Label(frame, text="Género:", bg="#FFFFFF", font=("Arial", 12))
        self.labelGenero.grid(row=1, column=2, padx=5, pady=5, sticky="e")

        self.genero_var = tk.StringVar()
        self.genero_select = ttk.Combobox(frame, textvariable=self.genero_var, values=["H", "M"], font=("Arial", 12), width=5, state="readonly")
        self.genero_select.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.genero_select.current(0)

        buttonFrame = tk.Frame(frame, bg="#FFFFFF")
        buttonFrame.grid(row=2, column=0, columnspan=4, pady=5)
        
        self.botonMedir = tk.Button(buttonFrame, text="Iniciar", bg="#4CAF50", fg="white", font=("Arial", 11), width=10, relief=tk.FLAT, command=self.iniciar_lectura_serial)
        self.botonMedir.pack(side=tk.LEFT, padx=5, pady=5)

        self.botonDetener = tk.Button(buttonFrame, text="Detener", bg="#D32F2F", fg="white", font=("Arial", 11), width=10, relief=tk.FLAT, command=self.detener_lectura_serial)
        self.botonDetener.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.botonSeleccionar = tk.Button(buttonFrame, text="Seleccionar", bg="#FF9800", fg="white", font=("Arial", 11), width=10, relief=tk.FLAT, command=self.detener_lectura_serial)
        self.botonSeleccionar.pack(side=tk.LEFT, padx=5, pady=5)
    
    def iniciar_lectura_serial(self):
        try:
            #self.ser = serial.Serial(self.puerto_serie, self.baudrate)
            print('Conexión correcta')
            #self.ser.write(b'1')  # Inicia la transmisión de datos
            self.valores = []
            self.leyendo = True
            self.etiqueta.config(text="Tomando datos...")
            
            self.hilo = Thread(target=self.leer_datos)
            self.hilo.start()
        except serial.SerialException as e:
            self.etiqueta.config(text="Error de conexión")
            print(f"Error: {str(e)}")
        except Exception as e:
            self.etiqueta.config(text="Ocurrió un error")
            print(f"Error: {str(e)}")
    
    def leer_datos(self):
        while self.leyendo:
            if self.ser.in_waiting > 0:
                dato = self.ser.readline().decode('utf-8').strip()
                self.valores.append(int(dato))
        
    def detener_lectura_serial(self):
        self.leyendo = False
        if self.ser:
            self.ser.write(b'0')  # Detiene la transmisión de datos
            self.ser.close()
        
        # Guardar datos en un archivo .mat
        datos = {"valores": np.array(self.valores)}
        sio.savemat(self.archivo_path, datos)
        
        print("Toma de muestras finalizada.")
        self.etiqueta.config(text="Muestras guardadas en .mat")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lectura Serial")
    root.configure(bg="#FFFFFF")
    ancho_ventana = 1020
    alto_ventana = 580
    x_pos = (root.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y_pos = (root.winfo_screenheight() // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
    app = SerialReader(root, "datos.mat", "/dev/rfcomm0", 9600)
    root.mainloop()
