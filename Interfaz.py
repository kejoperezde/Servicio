import tkinter as tk
from tkinter import messagebox

def centrar_ventana(ventana, ancho, alto):
    # Obtener el tamaño de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    # Calcular las coordenadas x, y para centrar la ventana
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    
    # Aplicar la geometría
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def iniciar_cuenta_regresiva():
    # Crear una nueva ventana para la cuenta regresiva
    ventana_cuenta = tk.Toplevel()
    ventana_cuenta.title("Esperando")
    ventana_cuenta.geometry("280x60")
    centrar_ventana(ventana_cuenta, 280, 60)  # Centrar la ventana de cuenta regresiva
    
    # Variable para el contador
    contador = 10

    def actualizar_cuenta():
        nonlocal contador
        if contador > 0:
            etiqueta.config(text="Tomando muestra... " + str(contador))
            contador -= 1
            ventana_cuenta.after(1000, actualizar_cuenta)  # Llama a esta función de nuevo después de 1 segundo
        else:
            etiqueta.config(text="Tomando muestra... ")
            ventana_cuenta.destroy()  # Cierra la ventana al llegar a 0

    # Etiqueta para mostrar el tiempo restante
    etiqueta = tk.Label(ventana_cuenta, font=("Helvetica", 14))
    etiqueta.pack(pady=20)

    # Iniciar la cuenta regresiva
    actualizar_cuenta()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica")
ventana.geometry("300x200")
centrar_ventana(ventana, 300, 200)  # Centrar la ventana principal

# Crear un botón y asignarle la función iniciar_cuenta_regresiva
boton = tk.Button(ventana, text="Tomar muestra", command=iniciar_cuenta_regresiva)
boton.pack(pady=20)

# Ejecutar el bucle principal
ventana.mainloop()
