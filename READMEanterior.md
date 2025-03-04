 

# Índice

- [Índice](#índice)
- [---------------- Sección artículo ----------------](#-----------------sección-artículo-----------------)
  - [1. Introducción](#1-introducción)
  - [2. Metodología](#2-metodología)
    - [2.1 **Transmisor**](#21-transmisor)
    - [2.2 \*\*\*\*](#22-)
    - [2.2 **Transmisión de datos**](#22-transmisión-de-datos)
    - [2.3 **Receptor y Sistema de Procesamiento**](#23-receptor-y-sistema-de-procesamiento)
- [---------------- Sección artículo ----------------](#-----------------sección-artículo------------------1)
  - [1. Introducción](#1-introducción-1)
    - [1.1. Objetivos del proyecto](#11-objetivos-del-proyecto)
    - [1.2. Importancia de la adquisición de señales ECG](#12-importancia-de-la-adquisición-de-señales-ecg)
    - [1.3. Alcance del proyecto](#13-alcance-del-proyecto)
  - [2. Fundamentos Teóricos](#2-fundamentos-teóricos)
    - [2.1. Qué es un ECG](#21-qué-es-un-ecg)
      - [2.1.1. Principios de funcionamiento](#211-principios-de-funcionamiento)
      - [2.1.2. Eithoven Triangle](#212-eithoven-triangle)
      - [2.1.3. Componentes de la señal ECG](#213-componentes-de-la-señal-ecg)
    - [2.2. Sistemas de adquisición de datos (DAQ)](#22-sistemas-de-adquisición-de-datos-daq)
      - [2.2.1. Definición y funciones](#221-definición-y-funciones)
    - [3.2. Sistemas de adquisición de datos (DAQ)](#32-sistemas-de-adquisición-de-datos-daq)
      - [3.2.1. Definición y funciones](#321-definición-y-funciones)
      - [3.2.2. Tipos de sistemas DAQ](#322-tipos-de-sistemas-daq)
    - [3.3. Introducción a sistemas embebidos](#33-introducción-a-sistemas-embebidos)
      - [3.3.1. Definición y características](#331-definición-y-características)
      - [3.3.2. Lenguaje C en sistemas embebidos](#332-lenguaje-c-en-sistemas-embebidos)
  - [3. Diseño del Sistema](#3-diseño-del-sistema)
    - [3.1. Selección de componentes](#31-selección-de-componentes)
    - [3.3. Esquema del sistema](#33-esquema-del-sistema)
  - [4. Desarrollo del Software](#4-desarrollo-del-software)
    - [4.1. Entorno de desarrollo](#41-entorno-de-desarrollo)
      - [4.1.1. Herramientas necesarias](#411-herramientas-necesarias)
        - [Screen](#screen)
        - [Dispositivos conectados](#dispositivos-conectados)
      - [4.1.2. Instalación y configuración](#412-instalación-y-configuración)
        - [Pop OS](#pop-os)
        - [Python](#python)
        - [Visual Studio Code](#visual-studio-code)
        - [Blueman](#blueman)
    - [4.2. Programación en Python](#42-programación-en-python)
      - [4.2.1. Estructura básica del programa](#421-estructura-básica-del-programa)
      - [4.2.2. Adquisición de datos](#422-adquisición-de-datos)
      - [4.2.3. Procesamiento de señales](#423-procesamiento-de-señales)
    - [4.3. Interfaz de usuario](#43-interfaz-de-usuario)
      - [4.3.1. Visualización de datos](#431-visualización-de-datos)
      - [4.3.2. Interacción con el sistema](#432-interacción-con-el-sistema)
  - [5. Implementación del Sistema](#5-implementación-del-sistema)
    - [5.1. Integración de hardware y software](#51-integración-de-hardware-y-software)
    - [5.2. Pruebas y validación](#52-pruebas-y-validación)
      - [5.2.1. Metodología de pruebas](#521-metodología-de-pruebas)
      - [5.2.2. Resultados obtenidos](#522-resultados-obtenidos)
  - [6. Análisis de Resultados](#6-análisis-de-resultados)
    - [6.1. Análisis de los datos adquiridos](#61-análisis-de-los-datos-adquiridos)
    - [6.2. Comparación con datos clínicos](#62-comparación-con-datos-clínicos)
    - [6.3. Evaluación del rendimiento del sistema](#63-evaluación-del-rendimiento-del-sistema)
    - [6.4. Interpretación de resultados](#64-interpretación-de-resultados)
  - [7. Discusión](#7-discusión)
    - [7.1. Limitaciones del sistema](#71-limitaciones-del-sistema)
    - [7.2. Posibilidades de mejora](#72-posibilidades-de-mejora)
    - [7.3. Aplicaciones futuras](#73-aplicaciones-futuras)
  - [8. Conclusiones y Futuras Direcciones](#8-conclusiones-y-futuras-direcciones)
    - [8.1. Conclusiones del proyecto](#81-conclusiones-del-proyecto)
    - [8.2. Posibles mejoras y desarrollos futuros](#82-posibles-mejoras-y-desarrollos-futuros)
    - [8.3. Impacto potencial en la salud y tecnología](#83-impacto-potencial-en-la-salud-y-tecnología)
  - [9. Referencias](#9-referencias)
    - [9.2. Fuentes de información](#92-fuentes-de-información)
    - [9.3. Recursos adicionales](#93-recursos-adicionales)
  - [10. Anexos](#10-anexos)
    - [10.1. Códigos fuente](#101-códigos-fuente)
    - [10.2. Diagramas y esquemas eléctricos](#102-diagramas-y-esquemas-eléctricos)
    - [10.3. Documentación adicional](#103-documentación-adicional)
    - [10.4. Resultados adicionales de pruebas](#104-resultados-adicionales-de-pruebas)
    - [10.5. Diagramas y gráficos](#105-diagramas-y-gráficos)
  - [11. Solución de problemas](#11-solución-de-problemas)
- [Cochinero util](#cochinero-util)


# ---------------- Sección artículo ----------------

## 1. Introducción

## 2. Metodología

Texto

### 2.1 **Transmisor**

El transmisor permite capturar la señal cardíaca y enviarla inalámbricamente

* Esquema, integrando todo lo siguiente

- Raspberry Pi Pico
> Es una microcontroladora compacta basada en el chip RP2040, Cuenta con un procesador ARM Cortex-M0+ de doble núcleo, 26 pines GPIO, y soporte para interfaces como I2C, SPI, y UART. Es compatible con MicroPython y C/C++.

- AD8232
> Es un módulo de sensor de señal bioeléctrica diseñado para medir la actividad eléctrica del corazón mediante un electrocardiograma (ECG)

- Módulo Bluetooth: RN-41-FLY-477
> El módulo RN-41-FLY-477 es un módulo Bluetooth de clase 1 diseñado para aplicaciones industriales y de bajo consumo

- Capacitor de poliéster de  0.1 uF a 250 volts
> Para transferir señales de un circuito a otro sin permitir que pase corriente continua, lo que permite que solo pase la señal alterna

- Electrodos: Ambiderm T715
> Electrodo Desechable autoadheible para monitoreo cardiaco con broche redondo Ambiderm, espuma de Polietileno, redondo, diámetro 55mm

- Cable de electródo DC 3.5
> Permite transmitir las señales captadas por los electrodos al adc mediante una conexión 3.5

- Requisitos del DAD
> Alimentación 5v (En este caso la amientación se dio mediante la conección usb tipo c de la raspberry pi pico)



### 2.2 ****

### 2.2 **Transmisión de datos**

General, tipos de transmisión de datos y el por que de cada uno

- Adquisicón
  
- UART (Universal Asynchronous Receiver/Transmitter)
  
- Bluetooth
  

### 2.3 **Receptor y Sistema de Procesamiento**

# ---------------- Sección artículo ----------------


## 1. Introducción

 En el presente proyecto se plantea el desarrollo de un sistema de adquisición de datos (DAQ) especializado en la obtención de señales electrocardiográficas (ECG) mediante el uso de sistemas embebidos y el lenguaje de programación C. Este sistema está diseñado para capturar la señal ECG de una persona, transmitirla a una computadora para su visualización y análisis, y, mediante algoritmos, detectar posibles anomalías cardíacas. A continuación, se abordan los aspectos clave del proyecto, incluyendo sus objetivos, importancia, y alcance, así como los fundamentos teóricos necesarios para su desarrollo.

### 1.1. Objetivos del proyecto

Desarrollo de un sistema electrónico para la adquisición de una señal ECG y un sistema de adquisición de datos (DAQ) para la obtención y procesamiento de señales ECG en tiempo real, utilizando sistemas embebidos programados en lenguaje C. Se busca que el sistema capture de manera precisa las señales electrocardiográficas de una persona, las transmita a una computadora para su visualización, y aplique algoritmos para analizar las señales y detectar posibles anomalías cardíacas.

### 1.2. Importancia de la adquisición de señales ECG

"La señal del ECG se ha analizado y utilizado para diversos fines, como la medición de la frecuencia cardíaca, el examen del ritmo de los latidos del corazón, el diagnóstico de anomalías cardíacas, el reconocimiento de emociones y la identificación biométrica" (Kaplan Berkaya et al., 2018).

"El ECG se debe considerar como una herramienta y no como un fin en sí mismo" (Hampton, 2013).

### 1.3. Alcance del proyecto

El dispositivo capturará la señal electrocardiográfica de una persona y enviará los datos a una computadora, donde serán procesados y visualizados mediante una interfaz gráfica. Además, el sistema integrará algoritmos para analizar las señales y detectar posibles anomalías cardíacas, dando información necesaria en caso de identificar patrones asociados a enfermedades. Los resultados del análisis serán evaluados a través de pruebas en sujetos de prueba para validar la precisión y funcionalidad del sistema.

[⇧ Volver al índice](#índice)

## 2. Fundamentos Teóricos

### 2.1. Qué es un ECG

"«ECG» son las siglas de electrocardiograma, o electrocardiografía" (Hampton, 2013).

"El electrocardiograma es un registro que refleja la actividad eléctrica del corazón" (Uribe, Duque, 2010).

#### 2.1.1. Principios de funcionamiento

"La  contracción  de  cualquier  músculo  se  asocia  a cambios  eléctricos  denominados  «despolarización», que  pueden  detectarse  mediante  electrodos  unidos a la superficie corpora" (Hampton, 2013). El corazón al tratarse de un músculo, también emite cambios electrónicos mientras está en funcionamiento, los cuales pueden ser medidos con ayuda de electrodos ubicados adecuadamente, tomando en cuenta que los demás músculos al también emitir cambios eléctricos deben estar estos en funcionameinto nulo para evitar intervenir con la señal emitida por el corazón.

#### 2.1.2. Eithoven Triangle

La actividad eléctrica del coración puede ser estuduada con electródos, un electródo son dispositivos que se colocan en la superficie de la piel para registrar la actividad eléctrica del corazón, su función es captar los impulsos eléctricos que genera el corazón.

La actividad eléctrica puede ser transmitida por los tejidos, esto depende de los polos que tengan los electrodos o las derivaciones.

![Triángulo de Einthoven](https://github.com/kejoperezde/Servicio/blob/main2/README/triangulo.png "Triángulo de Einthoven")
(Hernand, 2022)

#### 2.1.3. Componentes de la señal ECG

Derivaciones

### 2.2. Sistemas de adquisición de datos (DAQ)

#### 2.2.1. Definición y funciones

1.  Descargar sdk para Raspberry Pi Principios
    Desacargar [pico.sh](https://github.com/kejoperezde/Servicio/blob/3e0f7b95ebaf8ff6d712780103dedfb72edc734b/PICO/pico.sh)

    `chmod +x pico.sh`
    
    `./pico.sh`

2.  Descargar Pico Project Generator
    
    `cd /pico`

    `git clone https://github.com/raspberrypi/pico-project-generator.git`

3.  Ejecutar creador de proyectos C
    
    `cd /pico-project-generator`
  
    `./pico-project.py --gui`

### 3.2. Sistemas de adquisición de datos (DAQ)

#### 3.2.1. Definición y funciones

#### 3.2.2. Tipos de sistemas DAQ

### 3.3. Introducción a sistemas embebidos

#### 3.3.1. Definición y características

#### 3.3.2. Lenguaje C en sistemas embebidos


[⇧ Volver al índice](#índice)

## 3. Diseño del Sistema

### 3.1. Selección de componentes

### 3.3. Esquema del sistema

- ![Esquema](https://github.com/kejoperezde/Servicio/blob/0bd88815d1d097b9d29344461a53910fb38639e7/README/esquema.jpg "Esquema")

[⇧ Volver al índice](#índice)


## 4. Desarrollo del Software 

### 4.1. Entorno de desarrollo

- Visual Estudio Code

#### 4.1.1. Herramientas necesarias

- Laptop
- Sistema operativo Linux, distribución Pop Os

##### Screen

Sirve para gestionar sesiones de terminal 

1. Instalar screen (Opcional)
    
    `sudo apt install screen`

2. Ver sesión (datos recibidos)
    
    `sudo screen /dev/K` -> K dispositivo de entrada

##### Dispositivos conectados

1. Ver todos los dispotivios

    `ls /dev/tty*`

2. Dispositivos USB

    `ls /dev/ttyUSB*`

3. Dispositivos bluetooth

    `ls /dev/rfcomm*`

#### 4.1.2. Instalación y configuración

Texto

##### Pop OS

Es una distribución de Linux desarrollada por System76. Está diseñada para ser una opción confiable y eficiente para desarrolladores, creadores y usuarios de STEM (ciencia, tecnología, ingeniería y matemáticas).

1. Instalación de Pop OS (Versión usada: 22.04 lts)
    
    [pop.system76.com](https://pop.system76.com/ "Pop Os").

2. Actualización del sistema
    
    `sudo apt update && sudo apt upgrade`
    
3. Añadir usuario
    
    `sudo usermod -a -G dialout $USER`

4. Reiniciar
  
    `sudo reboot`

##### Python

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.

1. Instalar python 3 (Versión usada: 22.0.2)
    
    `sudo apt install python3-pip`

2. Librerías necesarias de python
    
    `pip install pyserial numpy pandas matplotlib`

    `pip3 install pyserial numpy pandas matplotlib`
  
    `sudo apt install python3-tk`

    `pip install pycryptodome`

3. Instalar pybluez

    1. `pip3 install setuptools==57.0.0`

    2. `sudo apt install libbluetooth-dev`

    3. `pip3 install pybluez`
 4. sudo apt-get install libsystemd-dev
4. pip3 install --upgrade systemd-python
sudo apt-get install python3-dev
pip3 install scipy
pysimplegui

  | Librería   | Versión | Descripción |
  | ---------- | ------- |------------ |
  | pyserial   | 3.5     | Para comunicación serial con dispositivos, como puertos serie o USB. |
  | numpy      | 2.1.3   | Para operaciones matemáticas y manipulación de arreglos y matrices. |
  | pandas     | 2.2.3   | Para manipulación y análisis de datos estructurados, como tablas y series temporales. |
  | matplotlib | 3.9.2   | Para crear gráficos y visualizaciones de datos. |
  | tkinter    | 3.10.8  | Para crear interfaces gráficas de usuario (GUI) |
  | pybluez    | 0.23    | Para comunicación Bluetooth en Python. |

##### Visual Studio Code

Es un editor de código fuente gratuito, ligero y multiplataforma desarrollado por Microsoft.

1. Instalar visual studio code (Versión usada: 1.95.2)

    `sudo apt install code`

2. Actualizar a última versión visual estudio code
    
    `sudo apt upgrade code`

##### Blueman

Es un administrador de Bluetooth para sistemas Linux.

1. Instalar blueman (Versión usada: 2.2.4)
    
    `sudo apt install blueman`

### 4.2. Programación en Python

#### 4.2.1. Estructura básica del programa

#### 4.2.2. Adquisición de datos

#### 4.2.3. Procesamiento de señales

### 4.3. Interfaz de usuario

#### 4.3.1. Visualización de datos

#### 4.3.2. Interacción con el sistema


[⇧ Volver al índice](#índice)

## 5. Implementación del Sistema

### 5.1. Integración de hardware y software

### 5.2. Pruebas y validación

#### 5.2.1. Metodología de pruebas

#### 5.2.2. Resultados obtenidos


[⇧ Volver al índice](#índice)

## 6. Análisis de Resultados

### 6.1. Análisis de los datos adquiridos

### 6.2. Comparación con datos clínicos

### 6.3. Evaluación del rendimiento del sistema

### 6.4. Interpretación de resultados


[⇧ Volver al índice](#índice)

## 7. Discusión

### 7.1. Limitaciones del sistema

### 7.2. Posibilidades de mejora

### 7.3. Aplicaciones futuras


[⇧ Volver al índice](#índice)

## 8. Conclusiones y Futuras Direcciones

### 8.1. Conclusiones del proyecto

### 8.2. Posibles mejoras y desarrollos futuros

### 8.3. Impacto potencial en la salud y tecnología


[⇧ Volver al índice](#índice)

## 9. Referencias

### 9.2. Fuentes de información

Uribe, William & Duque, Mauricio & Arango, Eduardo. (2010). Electrocardiografía y arritmias. Revista Iberoamericana de Arritmología. 10.5031/v1i2.RIA1012. 

Hampton, J. (2013). The ECG made easy. Elsevier Health Sciences.

Kaplan Berkaya, S., Uysal, A. K., Gunal, E. S., Ergin, S., Gunal, S., & Gulmezoglu, M. B. (2018). A survey on ECG analysis. Biomedical Signal Processing and Control, 43, 216-235. https://doi.org/10.1016/j.bspc.2018.03.003

KatlynMarceloHernand. (2022, 1 mayo). TRIANGULO DE EINTHOVEN. KATLYN MARCELO.pdf [Diapositivas]. SlideShare. https://es.slideshare.net/slideshow/triangulo-de-einthoven-katlyn-marcelopdf/251700420

### 9.3. Recursos adicionales

Imágenes [One Drive](https://1drv.ms/f/s!AsP3n41dk7dYgeCnVOpamzrRtiJD-2o?e=4rbqUR).

[⇧ Volver al índice](#índice)

## 10. Anexos

### 10.1. Códigos fuente

### 10.2. Diagramas y esquemas eléctricos

### 10.3. Documentación adicional

### 10.4. Resultados adicionales de pruebas

### 10.5. Diagramas y gráficos

## 11. Solución de problemas

Thonny (Opcional)

Es un entorno de desarrollo integrado (IDE) diseñado para programar en Python.

1. Instalar thonny (Versión usada: 2.1.21)
    
    `sudo apt install thonny`

3. Actualizar linux firmware (Tag usado: 20241110) OPCIONAL

    - Descargar última versión [linux-firmware](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git "linux-firmware").
    - Extraer contenido del archivo: `tar -xvf nombre_archivo.tar.yz`
    - Reemplazar archivos: `sudo cp -r /linux-firmware-####/* /lib/firmware`



CUDA
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local

Cudnn cuda-12
https://developer.nvidia.com/cudnn-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local

Sklearn
https://scikit-learn.org/1.5/install.html

TensorRT
https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/10.7.0/local_repo/nv-tensorrt-local-repo-ubuntu2204-10.7.0-cuda-12.6_1.0-1_amd64.deb

Pytorch

nvidia-smi
nvtop
sudo apt install nvtop

# Cochinero util
2. Procesamiento de señales con Wavelets

from pywt import wavedec

    pywt.wavedec: Función de la biblioteca PyWavelets que realiza la descomposición wavelet discreta.
        Esto se usa para descomponer una señal en diferentes niveles de detalle y obtener coeficientes wavelet.