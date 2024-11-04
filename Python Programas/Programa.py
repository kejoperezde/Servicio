import random
import csv

# Inicializar la lista y el contador
numeros_aleatorios = []
contador = 0

# Generar 8 números aleatorios usando un ciclo while
while contador < 8:
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)
    contador += 1

# Guardar los números en un archivo CSV
with open('numeros_aleatorios.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir los encabezados
    escritor_csv.writerow(['Índice', 'Número'])
    
    # Escribir los números en el archivo
    for indice, numero in enumerate(numeros_aleatorios):
        escritor_csv.writerow([indice + 1, numero])  # índice + 1 para comenzar desde 1

# Confirmación
print("Números aleatorios guardados en 'numeros_aleatorios.csv'.")

