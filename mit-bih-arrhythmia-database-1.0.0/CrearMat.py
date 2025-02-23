import os
import scipy.io as sio
import scipy.signal as signal
import numpy as np
import subprocess
import shutil
import math

# Lista de numeraciones a procesar
numeracion = [
    100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 
    117, 118, 119, 121, 122, 123, 124, 200, 201, 202, 203, 205, 207, 208, 209, 210, 
    212, 213, 214, 215, 217, 219, 220, 221, 222, 223, 228, 230, 231, 232, 233, 234
]

def ecgmain(path):
    """Carga la señal ECG desde un archivo .mat"""
    data = sio.loadmat(path)
    return data['val'].squeeze()

def resample(signal_ecg, original_fs=360, target_fs=192):
    """Remuestrea la señal a la frecuencia deseada."""
    num_samples = int(len(signal_ecg) * (target_fs / original_fs))
    return signal.resample(signal_ecg, num_samples)

def normalizar(signal):
    """Normaliza la señal ECG."""
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))

def latidos(normalizado):
    """Calcula la frecuencia cardíaca en latidos por minuto y por 10 segundos."""
    sampling_rate = 360
    peaks, _ = signal.find_peaks(normalizado, height=0.6, distance=sampling_rate*0.6)

    if len(peaks) > 1:
        rr_intervals = np.diff(peaks) / sampling_rate
        avg_rr = np.mean(rr_intervals)
        lpmaprox = 60 / avg_rr
        lpdiezseg = lpmaprox * (10 / 60)
        return lpmaprox, lpdiezseg
    else:
        return 60, 10  # Valores por defecto si no se detectan picos

def div_secciones(arr, num_secciones):
    """Divide la señal en secciones con redondeo personalizado."""

    # Redondeo basado en la parte decimal
    parte_entera = int(num_secciones)
    parte_decimal = num_secciones - parte_entera
    num_secciones = parte_entera if parte_decimal <= 0.4 else parte_entera + 1

    n = len(arr)
    tamaño_seccion = n // num_secciones
    sobrante = n % num_secciones

    secciones = []
    inicio = 0
    for i in range(num_secciones):
        extra = 1 if i < sobrante else 0
        fin = inicio + tamaño_seccion + extra
        secciones.append(arr[inicio:fin])
        inicio = fin

    return secciones

def encabezado(path):
    """Extrae la edad, género y enfermedades del archivo .hea."""
    with open(path + '.hea', 'r') as file:
        lines = file.readlines()
        age, sex, diseases = "Desconocida", "Desconocido", []

        for i, line in enumerate(lines):
            if line.startswith("#"):
                parts = line.split()
                if len(parts) >= 3 and parts[1].lstrip('-').isdigit():
                    age = parts[1] if int(parts[1]) > 0 else "Desconocida"
                    sex = "Masculino" if parts[2] == "M" else "Femenino"
                if i == 3 and len(parts) > 1:
                    diseases = [d.strip(',') for d in parts[1:]]
        return age, sex, diseases

def comando_wfdb2mat(numeracion):
    # Carpeta de salida
    output_dir = "wfdb_output"
    os.makedirs(output_dir, exist_ok=True)  # Crea la carpeta si no existe

    # Procesar cada muestra wfdb2mat para .mat
    for num in numeracion:
        command = f"wfdb2mat -r {num} -s 0 -f 00:00:00 -l 00:00:10"
        
        try:
            # Ejecutar el comando
            subprocess.run(command, shell=True, check=True)
            
            # Mover los archivos generados a la carpeta de salida
            for ext in ["m.mat", "m.hea"]:
                source_file = f"{num}{ext}"
                if os.path.exists(source_file):
                    shutil.move(source_file, os.path.join(output_dir, source_file))
        
        except subprocess.CalledProcessError as e:
            print(f"Error ejecutando wfdb2mat para {num}: {e}")

def datos_create(numeracion):
    # Crear carpeta para guardar los archivos si no existe
    output_dir = "datos_ecg"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Procesar cada muestra
    for num in numeracion:
        path_m = f"wfdb_output/{num}m"

        try:
            original = ecgmain(f"{path_m}.mat")
            resampled = resample(original, 360, 192)
            normalizado = normalizar(resampled)
            lpmaprox, lpdiezseg = latidos(normalizar(original))
            secciones = div_secciones(normalizado, lpdiezseg)
            age, sex, diseases = encabezado(path_m)

            # Datos a guardar
            data = {
                "normalizado": normalizado,
                "secciones": secciones,
                "sex": sex,
                "age": age,
                "diseases": diseases,
                "lpdiezseg": lpdiezseg,
            }

            # Guardar en un archivo específico dentro de la carpeta
            save_path = os.path.join(output_dir, f"datos_{num}.mat")
            sio.savemat(save_path, data)
            print(f"Archivo guardado: {save_path}")

        except Exception as e:
            print(f"Error procesando {num}: {e}")

# comando_wfdb2mat(numeracion)
datos_create(numeracion)