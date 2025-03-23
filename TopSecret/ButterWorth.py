import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

class ButterWorth:
    def __init__(self, fs=192, lowcut=0.5, highcut=40.0, order=4):
        """
        Inicializa la clase con los parámetros del filtro Butterworth.
        
        :param fs: Frecuencia de muestreo en Hz
        :param lowcut: Frecuencia de corte baja en Hz
        :param highcut: Frecuencia de corte alta en Hz
        :param order: Orden del filtro
        """
        self.fs = fs
        self.lowcut = lowcut
        self.highcut = highcut
        self.order = order
        self.nyquist = 0.5 * self.fs  # Frecuencia de Nyquist

        # Diseñar filtro pasa banda
        low = self.lowcut / self.nyquist
        high = self.highcut / self.nyquist
        self.b, self.a = signal.butter(self.order, [low, high], btype='band')

    def apply_filter(self, signal_data):
        """
        Aplica el filtro Butterworth a una señal de entrada.
        
        :param signal_data: Señal a filtrar (numpy array)
        :return: Señal filtrada
        """
        return signal.filtfilt(self.b, self.a, signal_data)

    def plot_signals(self, original_signal, filtered_signal, duration=10):
        """
        Grafica la señal original y la filtrada.
        
        :param original_signal: Señal original con ruido
        :param filtered_signal: Señal filtrada
        :param duration: Duración en segundos de la señal
        """
        t = np.linspace(0, duration, duration * self.fs, endpoint=False)

        plt.figure(figsize=(10, 5))
        plt.plot(t, original_signal, label="ECG con ruido", alpha=0.5)
        plt.plot(t, filtered_signal, label="ECG Filtrado", linewidth=2)
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Amplitud")
        plt.legend()
        plt.title("Filtrado de Señal ECG - Butterworth")
        plt.show()

# Prueba de la clase
if __name__ == "__main__":
    fs = 192  # Frecuencia de muestreo en Hz
    duration = 10  # Duración en segundos
    t = np.linspace(0, duration, duration * fs, endpoint=False)
    
    # Simular una señal ECG con ruido
    ecg_signal = np.sin(1.2 * 2 * np.pi * t) + 0.25 * np.random.randn(len(t))

    # Instanciar el filtro y aplicarlo
    filtro = ButterWorth(fs=fs)
    filtered_signal = filtro.apply_filter(ecg_signal)

    # Graficar la señal original y la filtrada
    filtro.plot_signals(ecg_signal, filtered_signal, duration)
