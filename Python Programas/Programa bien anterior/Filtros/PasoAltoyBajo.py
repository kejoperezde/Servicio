import pandas as pd
from scipy.signal import butter, filtfilt

class PasoAltoyBajo:
    
    def __init__(self, ruta_archivo, t_seg=10):
        self.ruta_archivo = ruta_archivo
        self.t_seg = t_seg  # Asignar t_seg como atributo de la clase

    # Filtrado de la señal (función de la clase debe tener self)
    def butter_lowpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs  # Frecuencia de Nyquist
        normal_cutoff = cutoff / nyq  # Normalización de la frecuencia de corte
        b, a = butter(order, normal_cutoff, btype='low', analog=False)  # Coeficientes del filtro
        return b, a

    def lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)  # Llamar a butter_lowpass con self
        y = filtfilt(b, a, data)  # Aplicación del filtro
        return y
    
    def aplicar_filtro(self):
        # Cargar los datos desde el archivo CSV
        dataset = pd.read_csv(self.ruta_archivo)
        
        signal = dataset['mV']
        # Configuración del filtro
        fs = len(signal) / self.t_seg  # Frecuencia de muestreo ajustada (190 Hz)
        cutoff = 40.0  # Frecuencia de corte ajustada (40 Hz)

        # Filtrar la señal
        filtered_signal = self.lowpass_filter(signal, cutoff, fs)  # Llamar a lowpass_filter con self
        
        return filtered_signal
