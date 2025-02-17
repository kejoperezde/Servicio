import wfdb  # Librería para leer archivos MIT-BIH
import numpy as np
import scipy.io as sio

def convertir_dat_a_mat(nombre_archivo, salida_mat):
    # Leer la señal ECG del archivo .dat y su frecuencia de muestreo
    registro = wfdb.rdrecord(nombre_archivo)
    
    # Extraer la señal (todas las derivaciones)
    ecg_data = registro.p_signal.T  # Transponer para que coincida con el formato de MATLAB
    
    # Crear estructura similar al archivo .mat que compartiste
    data_dict = {
        'ECG': np.array([[(  # Se guarda como un array de estructura similar
            np.array(['Male'], dtype='<U4'),  # Sexo (se coloca un valor por defecto)
            np.array([[30]], dtype=np.uint8),  # Edad (se coloca un valor por defecto)
            np.array(ecg_data)  # Matriz con las señales de ECG
        )]], dtype=[('sex', 'O'), ('age', 'O'), ('data', 'O')])
    }

    # Guardar el archivo como .mat
    sio.savemat(salida_mat, data_dict)
    print(f"Archivo guardado como {salida_mat}")

# Ejemplo de uso:
# convertir_dat_a_mat("100", "ecg_100.mat")  # Convierte el archivo 100.dat a ecg_100.mat

anotaciones = wfdb.rdann("100", "atr")  # Lee las anotaciones del archivo 100.atr
print(anotaciones.sample)  # Imprime las posiciones de las anotaciones
print(anotaciones.symbol)  # Imprime los símbolos de las anotaciones
