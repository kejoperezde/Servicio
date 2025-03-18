# Índice
## 1. Introducción

### 1.1. Objetivos del proyecto  

Desarrollo de un sistema electrónico para la adquisición de una señal ECG y un sistema de adquisición de datos (DAQ) para la obtención y procesamiento de señales ECG en tiempo real, utilizando sistemas embebidos programados en lenguaje C. Se busca que el sistema capture de manera precisa las señales electrocardiográficas de una persona, las transmita a una computadora para su visualización, y aplique algoritmos para analizar las señales y detectar posibles anomalías cardíacas. 

### 1.2. Justificación  
### 1.3. Importancia de la adquisición de señales ECG  

## 2. Fundamentos Teóricos
### 2.1 Frecuencia cardiaca  



### 2.2 Triángulo de Einthoven  
### 2.3 Electrocardiograma (ECG)  
### 2.4 Filtros digitales    
### 2.5 Convertidor ADC  
### 2.6 Sistemas de Adquisición de Datos (DAQ)  
### 2.7 Comunicación serie UART

## 3. Diseño del DAC
### 3.1 Componentes  
### 3.2 Microcontrolador  
### 3.3 Fuente de alimentación   
### 3.4 Diagrama  
### 3.5 Arquitectura del sistema

## 4. Entorno de desarrollo

### 4.1 Hardware de desarrollo

Laptop: Dell G15 5515
Procesador (CPU): Ryzen 7 5800H (8 núcleos / 16 hilos, hasta 4.2 GHz)
Gráficos (GPU): NVIDIA GeForce RTX 3060 (6GB GDDR6)
RAM: 16 DDR4, 3200MHz
Almacenamiento: SSD NVMe M.2 de 512 GB

### 4.2 Sistemas operativo: PopOS

Versión: Pop! OS 22.04 LTS
Kernel: 6.9.3-76060903-generic

Todo el desarrollo de código se llevo a cabo en la distrubución de linux Pop! Os, es gratuita y de código abierto, basada en ubuntu, desarrollada por System76, se utilizó esta debido a su estabilidad que tiene, recibe actualizaciones constantes, el kernel que tiene está actualizado para usarse con controladores gráficos de nvidia y amd. Además, está optimizada para cómputo científico, desarrollo de software e inteligencia artificial.

### 4.3 IDE: VS Code 

Version VSC: 1.96.0

Es un editor de código muy utilizado, agradable usabilidad, se le puede añadir múltiples extensiones que permiten generar código de mejor forma y más rápido.

### 4.4 Lenguajes de programación: C y Python  

En un inicio se utilizó el lenguaje python con ayuda de micropython por medio de Thonny para programar la raspberry, pero debido a que python es interpretado, hace que sea más lento, debido a esta desventaja, se decidió utilizar el lenguaje C para realizar toda la programación. Como ventajas de utilizar C es que al ser compilado, significa que se ejecuta directamente en el hardware, lo que hace que tenga un mejor desempeño. Teniendo un impaco directo en el dispositivo especificamente en la cantidad de datos enviados al programa. Donde si se utilizó python fue en el desarrollo del programa de adquisión, guardado y visualización de datos debido a su simplicidad y que contiene una amplia variedad útiles de librerías casi para desarrollar cualquier cosa.

### 4.5 Instalación de bibliotecas y configuración del entorno  



## 5. Programación del sistema embebido: C
### 5.1 Lectura y adquisición de datos  
### 5.2 Resolución, frecuencia de muestreo
### 5.3 Transmisión de datos: Comunicación en serie / bluetooth

## 6. Desarrollo de la aplicación en Python
### 6.1 Estructura del programa  
### 6.2 Lectura de datos transmitidos desde el DAC  
### 6.3 Interfaz de usuario
### 6.4 Controles de interacción (inicio/detención de adquisición)  
### 6.5 Guardado de datos a CSV
### 6.6 Filtrado digital (Butterworth)  
### 6.7 Visualización de datos

## 7. BD MIT BIH
### 7.1 Obtención de datos
### 7.2 WFDB2MAT
### 7.3 Procesado y guardado de muestras
### 7.4 Obtención de datos muestras

## 8. Resultados

## 9. Referencias

## 10. Anexos
### 10.1 Códigos fuente  
### 10.2 Gráficos adicionales  

## 11. Errores comunes y soluciones
### 11.1 Problemas en la adquisición de datos  
### 11.2 Fallos en la comunicación serie/Bluetooth  
### 11.3 Interferencias en la señal ECG  
