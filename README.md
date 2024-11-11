 

# Índice

- [Índice](#índice)
  - [1. Introducción](#1-introducción)
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
      - [2.2.2. Tipos de sistemas DAQ](#222-tipos-de-sistemas-daq)
    - [2.3. Introducción a sistemas embebidos](#23-introducción-a-sistemas-embebidos)
      - [2.3.1. Definición y características](#231-definición-y-características)
      - [2.3.2. Lenguaje C en sistemas embebidos](#232-lenguaje-c-en-sistemas-embebidos)
  - [3. Diseño del Sistema](#3-diseño-del-sistema)
    - [3.1. Requisitos del sistema](#31-requisitos-del-sistema)
    - [3.2. Esquema de bloques del sistema](#32-esquema-de-bloques-del-sistema)
    - [3.3. Selección de componentes](#33-selección-de-componentes)
      - [3.3.1. Sensores y electrodos](#331-sensores-y-electrodos)
      - [3.3.2. Microcontroladores y circuitos integrados](#332-microcontroladores-y-circuitos-integrados)
      - [3.3.3. Módulos de comunicación](#333-módulos-de-comunicación)
  - [4. Desarrollo del Software](#4-desarrollo-del-software)
    - [4.1. Entorno de desarrollo](#41-entorno-de-desarrollo)
      - [4.1.1. Herramientas necesarias](#411-herramientas-necesarias)
      - [4.1.2. Instalación y configuración](#412-instalación-y-configuración)
    - [4.2. Programación en C](#42-programación-en-c)
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

#### 2.2. Eithoven Triangle

La actividad eléctrica del coración puede ser estuduada con electródos, un electródo son dispositivos que se colocan en la superficie de la piel para registrar la actividad eléctrica del corazón, su función es captar los impulsos eléctricos que genera el corazón.

La actividad eléctrica puede ser transmitida por los tejidos, esto depende de los polos que tengan los electrodos o las derivaciones.




#### 2.1.3. Componentes de la señal ECG

Derivaciones

### 2.2. Sistemas de adquisición de datos (DAQ)

#### 2.2.1. Definición y funciones

#### 2.2.2. Tipos de sistemas DAQ

### 2.3. Introducción a sistemas embebidos

#### 2.3.1. Definición y características

#### 2.3.2. Lenguaje C en sistemas embebidos


[⇧ Volver al índice](#índice)

## 3. Diseño del Sistema

### 3.1. Requisitos del sistema

### 3.2. Esquema de bloques del sistema

### 3.3. Selección de componentes

#### 3.3.1. Sensores y electrodos

#### 3.3.2. Microcontroladores y circuitos integrados

#### 3.3.3. Módulos de comunicación


[⇧ Volver al índice](#índice)

## 4. Desarrollo del Software 

### 4.1. Entorno de desarrollo

- Visual Estudio Code

#### 4.1.1. Herramientas necesarias

- Laptop
- Sistema operativo Pop Os

#### 4.1.2. Instalación y configuración

1. Actualización del sistema
  > `sudo apt update && sudo apt upgrade -y`
2. Instalar python
  > `sudo apt install python3-pip`
3. Librerías necesarias de python
  > `sudo apt-get install python3-tk`

  - Para crear interfaces gráficas de usuario (GUI)

  > `pip3 install pyserial numpy pybluez pandas matplotlib`

  - **pyserial**: Para comunicación serial con dispositivos, como puertos serie o USB.
  - **numpy**: Para operaciones matemáticas y manipulación de arreglos y matrices.
  - **pybluez**: Para comunicación Bluetooth en Python (compatible principalmente con Linux y algunas versiones de Windows).
  - **pandas**: Para manipulación y análisis de datos estructurados, como tablas y series temporales.
  - **matplotlib**: Para crear gráficos y visualizaciones de datos.

4. Instalar Thonny (Opcional)
  > `sudo apt install thonny`

5. Añadir usuario (**Después reiniciar**)
  > `sudo usermod -a -G dialout $USER`

6. Instalar visual estudio code
  > `sudo apt-get install code -y`

7. Instalar screen (Opcional)
  > `sudo apt-get install screen`

8. Ver sesión (datos recibidos)
  > `sudo screen /dev/ttyK` -> K dispositivo de entrada

9. Ver puertos
  > `ls /dev/ tty*` y `ls /dev/ttyUSB*`

10. Descargar sdk para Raspberry Pi Principios
 > Desacargar [pico.sh](https://github.com/kejoperezde/Servicio/blob/3e0f7b95ebaf8ff6d712780103dedfb72edc734b/PICO/pico.sh)
 >
 > `chmod +x pico.sh`

11. Ejecutar creador de proyectos C
  > `cd /pico/pico-project-generator`
  >
  > `./pico_project.py --gui`

### 4.2. Programación en C

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

### 9.3. Recursos adicionales

Imágenes [One Drive](https://1drv.ms/f/s!AsP3n41dk7dYgeCnVOpamzrRtiJD-2o?e=4rbqUR).

[⇧ Volver al índice](#índice)

## 10. Anexos

### 10.1. Códigos fuente

### 10.2. Diagramas y esquemas eléctricos

### 10.3. Documentación adicional

### 10.4. Resultados adicionales de pruebas

### 10.5. Diagramas y gráficos
