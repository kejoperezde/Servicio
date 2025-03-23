import pandas as pd
class PromedioMovil:
    
    def __init__(self, ruta_archivo, rango=2):
        self.ruta_archivo = ruta_archivo
        self.rango = rango


    def aplicar_filtro(self):
    
        dataset = pd.read_csv(self.ruta_archivo)

        # Definir el tamaño de la ventana del promedio móvil
        r = self.rango
        
        # Calcular el promedio móvil y agregarlo al dataframe
        dataset['promedio_movil'] = dataset['mV'].rolling(window=r).mean()

        # Extraer las columnas
        movil = dataset['promedio_movil']
        
        return movil
