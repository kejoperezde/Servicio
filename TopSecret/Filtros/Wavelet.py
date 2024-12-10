import pandas as pd
import pywt

class Wavelet:
    
    def __init__(self, ruta_archivo, wavelet='db4', level=2, threshold=0.06):
        """
        Inicializa la clase con la ruta del archivo, la wavelet, el nivel de descomposición y el umbral.
        - ruta_archivo: Ruta del archivo CSV con los datos.
        - wavelet: Nombre de la wavelet a utilizar (por defecto 'db4').
        - level: Nivel de descomposición (por defecto 5).
        - threshold: Valor de umbral para la umbralización (por defecto 0.05).
        """
        self.ruta_archivo = ruta_archivo
        self.wavelet = wavelet
        self.level = level
        self.threshold = threshold
    
    def aplicar_filtro(self):
        """
        Aplica el filtro wavelet a la señal ECG.
        """
        # Cargar los datos desde el archivo CSV
        dataset = pd.read_csv(self.ruta_archivo)
        
        # Obtener la señal de la columna 'mV' (suponiendo que el archivo tiene esta columna)
        signal = dataset['mV'].values
        
        
        # Realizar la descomposición wavelet
        coeffs = pywt.wavedec(signal, self.wavelet, level=self.level)
        
        # Umbralización: establecer a cero los coeficientes pequeños
        coeffs_thresholded = [pywt.threshold(c, self.threshold, mode='soft') for c in coeffs]
        
        # Reconstruir la señal utilizando los coeficientes umbralizados
        filtered_signal = pywt.waverec(coeffs_thresholded, self.wavelet)
        
        # Asegurar que la señal filtrada tenga el mismo tamaño que la original
        filtered_signal = filtered_signal[:len(signal)]
        
        return filtered_signal

