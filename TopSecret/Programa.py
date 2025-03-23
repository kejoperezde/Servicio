import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Funciones import *

# Configuración de variables globales
PUERTO_SERIE = '/dev/rfcomm0'  # Cambiar puerto según configuración
BAUDRATE = 9600

class ECGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Programa ECG")
        centrar_ventana(self.root, 1500, 480)
        self.root.configure(bg="#f0f0f0")
        
        self.crear_widgets()
        self.crear_grafico()
    
    def crear_widgets(self):
        """ Crea los elementos de la interfaz gráfica con mejor distribución """
        frame_controles = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame_controles.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        # Etiqueta y entrada de nombre
        tk.Label(frame_controles, text="Nombre:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_name = tk.Entry(frame_controles, font=("Arial", 12))
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        
        # Etiqueta y entrada de edad
        tk.Label(frame_controles, text="Edad:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_age = tk.Entry(frame_controles, font=("Arial", 12))
        self.entry_age.grid(row=1, column=1, padx=5, pady=5)
        
        # Etiqueta y menú desplegable de género
        tk.Label(frame_controles, text="Género:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.generos = ["Masculino", "Femenino"]
        self.selected_genero = tk.StringVar(self.root)
        self.selected_genero.set(self.generos[0])  # Opción por defecto
        self.menu_genero = tk.OptionMenu(frame_controles, self.selected_genero, *self.generos)
        self.menu_genero.grid(row=2, column=1, padx=5, pady=5)
        
        # Botones con mejor distribución y diseño
        boton_frame = tk.Frame(self.root, bg="#ffffff", pady=10)
        boton_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        # Menú desplegable con opciones
        tk.Label(boton_frame, text="Fase:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.opciones = ["0. Prueba", "1. Baseline", "2. Stroop", "3. Pausa", "4. Respiracion"]
        self.selected_option = tk.StringVar(self.root)
        self.selected_option.set(self.opciones[0])  # Opción por defecto
        self.menu_opciones = tk.OptionMenu(boton_frame, self.selected_option, *self.opciones)
        self.menu_opciones.grid(row=0, column=1, padx=5, pady=5)
        
        # Botones
        boton_medir = tk.Button(boton_frame, text="Medir", bg="#28a745", fg="white", font=("Arial", 12, "bold"), width=15, command=self.medir)
        boton_medir.grid(row=1, column=0, padx=10, pady=10)
        
        boton_seleccionar = tk.Button(boton_frame, text="Seleccionar", bg="#fd7e14", fg="white", font=("Arial", 12, "bold"), width=15, command=self.seleccionar)
        boton_seleccionar.grid(row=1, column=1, padx=10, pady=10)
        
    
    def crear_grafico(self):
        """ Crea la figura de Matplotlib con un diseño mejorado """
        frame_grafico = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame_grafico.grid(row=0, column=1, rowspan=2, padx=20, pady=20)
        
        self.fig, self.ax = plt.subplots(figsize=(10, 4), facecolor='white')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 0.08)
        self.ax.set_title("Señal ECG", fontsize=14, fontweight='bold')
        self.ax.set_ylabel("Amplitud", fontsize=12)
        self.ax.set_xlabel("Segundos", fontsize=12)
        
        # Integrar el gráfico en la ventana
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame_grafico)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
    
    def medir(self): # Metodo perro
        # Recuperar datos
        selected_fase = self.selected_option.get() # Fase: ["0. Prueba", "1. Baseline", "2. Stroop", "3. Pausa", "4. Respiracion"]
        nombre = self.entry_name.get().strip() # Nombre
        edad = self.entry_age.get() # Edad
        genero = self.selected_genero.get() # Género: ["Masculino", "Femenino"]
        data = [] # Array de edad y genero: [21, "kevin"]
        
        # Validacion
        if not nombre:
            messagebox.showwarning("Advertencia", "Ponle un nombre a la muestra")
            return
        if not edad.isdigit():
            messagebox.showwarning("Advertencia", "La edad debe ser un número válido")
            return
        edad = int(edad)
        if edad < 1 or edad > 120:
            messagebox.showwarning("Advertencia", "La edad debe estar en rango")
            return
        
        path_archivo = crear_carpeta_y_archivo(nombre, selected_fase)
        
        if path_archivo != None:
            data.append([edad, genero])
            open_video(selected_fase)
            iniciar_lectura_serial(path_archivo, PUERTO_SERIE, BAUDRATE, selected_fase)
            graficar_datos(self.ax, self.canvas, path_archivo)
            
    def seleccionar(self):
        """ Permite seleccionar un archivo y graficar sus datos """
        archivo_path = seleccionar_archivo()
        if archivo_path:
            graficar_datos(self.ax, self.canvas, archivo_path)
            # graficar_filtros(archivo_path)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ECGApp(root)
    root.mainloop()

    