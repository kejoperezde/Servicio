from scipy.signal import butter, filtfilt
import pandas as pd

class ButterWorth:
    
    def __init__(self, ruta_archivo, t_seg=10):
        self.ruta_archivo = ruta_archivo
        self.t_seg = t_seg  # Frecuencia de muestreo
    
    def aplicar_filtro(self):
        # Cargar los datos desde el archivo CSV
        dataset = pd.read_csv(self.ruta_archivo)

        # Obtener la señal de la columna 'mV' (suponiendo que el archivo tiene esta columna)
        signal = dataset['mV']
        fs = len(signal) / self.t_seg
        
        # Establecer la frecuencia de corte para el filtro pasabajo
        cutoff_freq = 40  # Frecuencia de corte (ajustada a 40 Hz, más apropiado para ECG)
        
        # Calcular la frecuencia de Nyquist (mitad de la frecuencia de muestreo)
        nyquist_freq = 0.5 * fs  # fs es la frecuencia de muestreo
        
        # Normalizar la frecuencia de corte para el filtro de Butterworth
        normalized_cutoff = cutoff_freq / nyquist_freq
        
        # Definir el orden del filtro
        order = 4  # Orden del filtro (un valor de 4 es común para ECG)
        
        # Crear los coeficientes del filtro Butterworth
        b, a = butter(order, normalized_cutoff, btype='low')

        # Aplicar el filtro pasabajo a la señal
        filtered_signal = filtfilt(b, a, signal)
        
        # Retornar la señal filtrada
        return filtered_signal
