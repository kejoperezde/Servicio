### **1. Introducción**
1.1. Objetivos del proyecto

Desarrollo de un sistema electrónico para la adquisición de una señal ECG y un sistema de adquisición de datos (DAQ) para la obtención y procesamiento de señales ECG en tiempo real, utilizando sistemas embebidos programados en lenguaje C. Se busca que el sistema capture de manera precisa las señales electrocardiográficas de una persona, las transmita a una computadora para su visualización, y aplique algoritmos para analizar las señales y detectar posibles anomalías cardíacas. 

1.2. Importancia de la adquisición de señales ECG

La adquisición de señales electrocardiográficas (ECG) es fundamental en el monitoreo y diagnóstico de enfermedades cardiovasculares. Un sistema de adquisición de ECG permite registrar la actividad eléctrica del corazón a través de electrodos colocados en la piel, proporcionando información clave sobre el ritmo y la función cardíaca. La precisión en la adquisición de estas señales es esencial, ya que cualquier interferencia o ruido puede afectar la interpretación de los datos, lo que podría llevar a diagnósticos erróneos (García et al., 2015).

El desarrollo de sistemas de adquisición de ECG ha evolucionado significativamente gracias a los avances en electrónica y procesamiento de señales. La implementación de filtros digitales y amplificadores de instrumentación ha mejorado la calidad de las señales obtenidas, permitiendo una detección más precisa de anomalías como arritmias y bloqueos cardíacos (Rodríguez & López, 2020). Además, la integración de sistemas embebidos y la transmisión de datos en tiempo real han facilitado el monitoreo remoto, beneficiando a pacientes con enfermedades crónicas y reduciendo la necesidad de hospitalización (Fernández et al., 2018).

La importancia de la adquisición de señales ECG también radica en su uso en el ámbito de la investigación biomédica y el desarrollo de tecnologías médicas innovadoras. Los sistemas modernos de adquisición no solo permiten visualizar las señales en tiempo real, sino que también posibilitan el análisis automatizado mediante algoritmos de inteligencia artificial, mejorando la detección temprana de patologías (Martínez et al., 2019). Estos avances refuerzan la necesidad de continuar optimizando los sistemas de adquisición para lograr registros cada vez más precisos y accesibles en entornos clínicos y domésticos.

1.3. Alcance del proyecto

El presente proyecto tiene como objetivo el desarrollo de un sistema electrónico para la adquisición y análisis de señales electrocardiográficas (ECG), diseñado para fines de investigación biomédica. El sistema captura señales ECG mediante electrodos especializados, las transmite a una computadora para su almacenamiento y visualización, y aplica algoritmos de procesamiento para la detección de posibles anomalías cardíacas.

1.4. Justificación tecnológica  

El desarrollo de un sistema de adquisición de señales electrocardiográficas (ECG) basado en sistemas embebidos y procesamiento digital de señales responde a la necesidad de contar con herramientas accesibles y eficientes para la investigación biomédica. Actualmente, la adquisición y análisis de señales ECG requiere equipos de alto costo, diseñados principalmente para aplicaciones médicas certificadas. Este proyecto busca ofrecer una alternativa basada en hardware de bajo costo, manteniendo una alta precisión en la captura y procesamiento de datos.  

### **2. Fundamentos Teóricos**  

2.1. Qué es un ECG  

Un electrocardiograma (ECG) es un estudio diagnóstico que mide la actividad eléctrica del corazón mediante electrodos colocados en la piel, generando un trazado que representa las distintas fases del ciclo cardíaco. Este examen es ampliamente utilizado en la medicina para detectar alteraciones en el ritmo cardíaco, bloqueos de conducción, hipertrofias ventriculares y signos de isquemia o infarto de miocardio (Fundación Española del Corazón, s.f.). Además, el ECG permite evaluar la respuesta del corazón ante diferentes estímulos y sufre variaciones según las condiciones fisiológicas del paciente (MedlinePlus, s.f.).

2.1.1. Principios de funcionamiento

El electrocardiograma (ECG) es una herramienta diagnóstica que registra la actividad eléctrica del corazón a lo largo del tiempo, proporcionando información valiosa sobre su funcionamiento y posibles anomalías. Su funcionamiento se basa en la detección de las señales eléctricas generadas durante el ciclo cardíaco, las cuales son captadas por electrodos colocados en la superficie corporal y representadas gráficamente en un trazado que muestra las distintas fases del ciclo cardíaco (Mayo Clinic, s.f.).

Durante cada latido, el corazón experimenta una serie de eventos eléctricos que preceden a la contracción muscular. Estos eventos se inician en el nódulo sinoauricular (SA), ubicado en la aurícula derecha, que actúa como marcapasos natural al generar un impulso eléctrico. Este impulso provoca la despolarización de las aurículas, lo que conduce a su contracción y se refleja en el ECG como la onda P (Departamento de Fisiología, UNAM, s.f.).

Posteriormente, el impulso eléctrico llega al nódulo auriculoventricular (AV), donde se produce una breve demora que permite el llenado adecuado de los ventrículos. Desde el nódulo AV, la señal se transmite al haz de His y luego a las fibras de Purkinje, distribuyéndose por el miocardio ventricular y provocando la despolarización de los ventrículos. Este proceso se representa en el ECG como el complejo QRS, que indica la contracción ventricular (Departamento de Fisiología, UNAM, s.f.).

Finalmente, los ventrículos se repolarizan para prepararse para el siguiente ciclo cardíaco, lo que se manifiesta en el ECG como la onda T. La correcta interpretación de estas ondas y segmentos en el electrocardiograma es esencial para identificar posibles anomalías en la conducción eléctrica del corazón, como arritmias, bloqueos o isquemias (Departamento de Fisiología, UNAM, s.f.).

El ECG es una prueba no invasiva y de gran valor diagnóstico, utilizada ampliamente en la práctica clínica para evaluar la salud cardiovascular de los pacientes (Mayo Clinic, s.f.).
Referencias (Formato APA 7ma edición)

2.1.2. Triángulo de Einthoven

El triángulo de Einthoven es un modelo conceptual en electrocardiografía que describe la disposición de las derivaciones bipolares estándar utilizadas para registrar la actividad eléctrica del corazón. Este concepto fue introducido por Willem Einthoven, quien desarrolló el primer electrocardiógrafo funcional y estableció las bases de la electrocardiografía moderna (Departamento de Fisiología, UNAM, s.f.).  

**Formación del Triángulo de Einthoven**  

El triángulo de Einthoven se construye al conectar los electrodos colocados en las extremidades del paciente, formando un triángulo equilátero con el corazón en su centro. Las derivaciones bipolares estándar que lo conforman son:  

- **Derivación I (DI):** mide la diferencia de potencial entre el brazo derecho (RA) y el brazo izquierdo (LA).  
- **Derivación II (DII):** registra la diferencia de potencial entre el brazo derecho (RA) y la pierna izquierda (LL).  
- **Derivación III (DIII):** evalúa la diferencia de potencial entre el brazo izquierdo (LA) y la pierna izquierda (LL) (Sociedad Interamericana de Cardiología, s.f.).  

Estas derivaciones permiten analizar la propagación de los impulsos eléctricos en el plano frontal y son esenciales para la correcta interpretación del electrocardiograma (ECG).   

**Ley de Einthoven**  

Una característica fundamental del triángulo de Einthoven es la **Ley de Einthoven**, la cual establece que la suma de los potenciales eléctricos registrados en las derivaciones I y III es igual al potencial registrado en la derivación II (DII = DI + DIII). Esta relación matemática es útil para verificar la correcta colocación de los electrodos y la calidad de la señal registrada (Sociedad Interamericana de Cardiología, s.f.).  

**Aplicaciones Clínicas**  

La comprensión del triángulo de Einthoven y las derivaciones estándar es clave para múltiples aplicaciones en cardiología:  

- **Diagnóstico de arritmias:** permite identificar irregularidades en el ritmo cardíaco.  
- **Detección de isquemia o infarto:** observa cambios en el segmento ST y en la onda T que indican falta de irrigación sanguínea o daño miocárdico.  
- **Evaluación de bloqueos de conducción:** ayuda a detectar retrasos o bloqueos en la transmisión del impulso eléctrico en el corazón.  

El triángulo de Einthoven y las derivaciones estándar constituyen los pilares de la electrocardiografía, proporcionando una base fundamental para la interpretación precisa de la actividad eléctrica cardíaca y el diagnóstico de enfermedades cardiovasculares (Departamento de Fisiología, UNAM, s.f.).  
 
2.1.3. Ruido en la señal ECG

El electrocardiograma (ECG) es una herramienta esencial en la práctica clínica para el diagnóstico y monitoreo de diversas condiciones cardíacas. Sin embargo, la precisión de las señales ECG puede verse comprometida por la presencia de diversos tipos de ruido, lo que dificulta su correcta interpretación.

**Tipos de ruido en la señal ECG**

Las señales ECG pueden verse afectadas por diferentes fuentes de ruido, entre las que se destacan:

1. **Interferencia de la línea de potencia:** Esta interferencia, originada por la red eléctrica, se manifiesta como una señal sinusoidal de 50 o 60 Hz superpuesta al ECG. Su presencia puede enmascarar componentes importantes de la señal cardíaca, afectando la precisión diagnóstica (Martínez Romo et al., 2008).

2. **Ruido electromiográfico (EMG):** Producido por la actividad muscular del paciente, este ruido se caracteriza por su naturaleza transitoria y puede confundirse con eventos cardíacos reales, especialmente en situaciones de contracción muscular involuntaria (Vázquez Seisdedos et al., 2010).

3. **Artefactos por movimiento:** Los movimientos del paciente, como respiración o cambios de posición, pueden generar variaciones en la línea base del ECG, conocidas como desplazamiento de la línea base, dificultando la identificación de ondas y segmentos clave (Vázquez Seisdedos et al., 2010).

4. **Ruido por sudoración:** La humedad en la piel debido a la sudoración puede aumentar la impedancia entre el electrodo y la piel, generando ruido eléctrico aleatorio que afecta la calidad de la señal (Schiller, 2025).

**Importancia de la reducción de ruido en el ECG**

La presencia de ruido en las señales ECG puede conducir a diagnósticos erróneos, afectando la detección de arritmias, isquemias y otras patologías cardíacas. Por ello, es fundamental aplicar técnicas de procesamiento de señales que permitan obtener registros de alta calidad, garantizando la confiabilidad de las evaluaciones médicas (Vázquez Seisdedos et al., 2010).

El ruido en las señales ECG representa un desafío significativo en la práctica clínica. La implementación de técnicas avanzadas de procesamiento y filtrado es esencial para asegurar la precisión diagnóstica y la calidad de la atención al paciente.

2.1.4. Filtro utilizado en ECG ButterWorth

El **filtro Butterworth** es una de las herramientas más utilizadas en el procesamiento de señales electrocardiográficas (ECG) debido a su característica de ofrecer una respuesta en frecuencia suavemente decreciente sin ondulaciones en la banda pasante. Esto permite que la señal ECG mantenga su integridad, minimizando la distorsión mientras se eliminan ruidos no deseados (González Murillo, 2014).  

**Características del Filtro Butterworth**  

El filtro Butterworth está diseñado para lograr una respuesta de magnitud máximamente plana en la banda pasante, evitando ondulaciones que podrían afectar la señal ECG. Su función de transferencia para un filtro pasa-bajos se expresa como:  

$|H(j\omega)|^2 = \frac{H_0^2}{1 + \left(\frac{\omega}{\omega_c}\right)^{2n}}$

- $|H(j\omega)|$ es la magnitud de la función de transferencia.  
- $H_0$ es la ganancia en la banda pasante.  
- $\omega$ es la frecuencia angular.  
- $\omega_c$ es la frecuencia de corte (-3 dB).  
- $n$ es el orden del filtro.  



Esta configuración asegura una transición suave entre las bandas pasante y de atenuación, lo que es esencial en aplicaciones biomédicas donde la preservación de la morfología de la señal es crítica (Ochoa et al., 2011).  

**Aplicación en el Filtrado de Señales ECG**  

Las señales ECG pueden verse afectadas por diversas fuentes de ruido, como la interferencia de la línea de potencia (50/60 Hz), el ruido electromiográfico y las variaciones de la línea base. El uso de un filtro Butterworth, tanto en configuraciones pasa-bajos como pasa-altos, ayuda a mitigar estas interferencias.  

Por ejemplo, en el diseño de un filtro pasa-banda para ECG, se pueden combinar un filtro pasa-altos de cuarto orden con una frecuencia de corte de 0.02 Hz y un filtro pasa-bajos de cuarto orden con una frecuencia de corte de 100 Hz. Esta configuración abarca el rango de frecuencias típico de la señal ECG, eliminando componentes no deseados sin distorsionar la señal de interés (Vásquez et al., 2007).  

**Ventajas del Filtro Butterworth en ECG**  

- **Respuesta Suave:** La ausencia de ondulaciones en la banda pasante asegura que la morfología de la señal ECG se mantenga intacta, facilitando su interpretación clínica.  
- **Transición Controlada:** La pendiente de atenuación en la banda de rechazo es suficientemente pronunciada para eliminar el ruido fuera de la banda de interés sin afectar la señal útil.  
- **Estabilidad y Facilidad de Diseño:** Sus características matemáticas facilitan su implementación en sistemas analógicos y digitales, garantizando estabilidad y rendimiento confiable.  

El filtro Butterworth es una de las mejores opciones para el procesamiento de señales ECG debido a su capacidad para preservar la integridad de la señal mientras elimina eficazmente interferencias. Su correcta implementación permite mejorar la calidad de los registros electrocardiográficos, asegurando diagnósticos más precisos y confiables en aplicaciones médicas y de investigación.  

2.2. **Sistemas de adquisición de datos (DAQ)**  

2.2.1. Definición y funciones 

Los **sistemas de adquisición de datos** (DAQ, por sus siglas en inglés) son herramientas esenciales en la medición y análisis de variables físicas, permitiendo la conversión de señales analógicas en datos digitales procesables por computadoras. Estos sistemas son ampliamente utilizados en áreas como la ingeniería, la investigación científica y la automatización industrial, facilitando la monitorización, control y análisis de diversos parámetros físicos y químicos (Dewesoft, s.f.).  

**Definición de Sistemas de Adquisición de Datos (DAQ)**  

Un sistema DAQ está compuesto por dispositivos y software diseñados para capturar y procesar señales provenientes del entorno, transformándolas en datos digitales que pueden ser analizados y almacenados en una computadora. Su función principal es permitir la recopilación de información sobre un fenómeno físico con el fin de documentarlo, analizarlo o controlarlo (Omega Engineering, s.f.).  

**Funciones Principales de un Sistema DAQ**  

1. **Medición de Variables Físicas:**  
   Los sistemas DAQ permiten la medición precisa de magnitudes como temperatura, presión, flujo y nivel, a través del uso de sensores específicos (Omega Engineering, s.f.).  

2. **Conversión de Señales:**  
   Transforman señales analógicas provenientes de sensores en datos digitales mediante **convertidores analógico-digitales (ADC)**, facilitando su procesamiento y almacenamiento.  

3. **Acondicionamiento de Señales:**  
   Incluyen etapas de acondicionamiento que permiten amplificar, filtrar o aislar la señal antes de su digitalización, garantizando que los datos adquiridos sean precisos y fiables (Dewesoft, s.f.).  

4. **Almacenamiento y Visualización de Datos:**  
   Permiten registrar y almacenar datos para su análisis posterior, así como su visualización en tiempo real, facilitando la interpretación y toma de decisiones en distintos contextos de aplicación (Siemens, s.f.).  

5. **Control y Automatización:**  
   Integran funciones de control en tiempo real, lo que permite su uso en procesos de automatización y supervisión industrial.  

**Componentes de un Sistema DAQ**  

Un sistema DAQ típico consta de los siguientes elementos:  

- **Sensores o Transductores:** Dispositivos que convierten una magnitud física en una señal eléctrica medible.  
- **Acondicionadores de Señal:** Modifican la salida de los sensores para adaptarla a los niveles requeridos por los ADC.  
- **Convertidores Analógico-Digitales (ADC):** Transforman las señales analógicas acondicionadas en datos digitales.  
- **Computadora con Software DAQ:** Permite el registro, visualización y análisis de los datos adquiridos.  

Los sistemas de adquisición de datos desempeñan un papel crucial en la medición, monitoreo y análisis de variables físicas. Su integración en diversas áreas ha permitido mejorar la eficiencia y precisión en la recopilación de datos, garantizando resultados confiables en aplicaciones industriales, científicas y de automatización.   

2.2.2. Tipos de sistemas DAQ  
2.2.3. Parámetros clave: resolución, frecuencia de muestreo, velocidad de conversión  
2.2.4. Conversión analógica a digital en señales biomédicas  

2.3. **Introducción a sistemas embebidos**  
2.3.1. Definición y características  
2.3.2. Tipos de microcontroladores utilizados en adquisición de señales biomédicas  
2.3.3. Lenguaje C en sistemas embebidos  
2.3.4. Comunicación serie (UART, SPI, I2C) en sistemas embebidos  

---

### **3. Diseño del Sistema**  
3.1. **Selección de componentes**  
3.1.1. Sensores de adquisición de ECG (electrodos, tipo de conexión, materiales)  
3.1.2. Amplificadores de instrumentación (Ejemplo: AD620, INA128)  
3.1.3. Filtros analógicos para reducción de ruido (Pasa-altas, pasa-bajas, notch 50/60Hz)  
3.1.4. Convertidores ADC y selección del DAC adecuado  
3.1.5. Microcontrolador o FPGA para adquisición y procesamiento  
3.1.6. Comunicación con PC o sistema de almacenamiento  

3.2. **Esquema del sistema**  
3.2.1. Diagrama de bloques del sistema  
3.2.2. Circuito del acondicionamiento de señal  
3.2.3. Interfaz del microcontrolador con el ADC y DAC  
3.2.4. Fuente de alimentación y consideraciones de seguridad  

---

### **4. Desarrollo del Software**  
4.1. **Entorno de desarrollo**  
4.1.1. Herramientas necesarias  
- Sistemas operativos compatibles (Windows, Linux, MacOS)  
- Lenguajes de programación (Python, C, C++)  
- IDEs utilizados (VS Code, Keil, Arduino IDE, etc.)  
4.1.2. Instalación y configuración  
- Configuración de entorno en Pop OS  
- Instalación de bibliotecas necesarias (NumPy, SciPy, Matplotlib)  
- Configuración de comunicación con el hardware (puertos seriales, Bluetooth, WiFi)  

4.2. **Programación en Python**  
4.2.1. Estructura básica del programa  
4.2.2. Adquisición de datos en tiempo real  
- Uso de bibliotecas (pySerial, pandas, etc.)  
- Lectura de datos desde el DAC  
- Procesamiento y filtrado de señales (FFT, wavelet transform)  
4.2.3. Procesamiento de señales  
- Filtrado digital (filtros FIR/IIR)  
- Eliminación de artefactos (movimiento, interferencia de línea)  
- Segmentación y análisis de ondas ECG  

4.3. **Interfaz de usuario**  
4.3.1. Visualización de datos en tiempo real  
- Uso de Matplotlib y PyQt5 para gráficos en vivo  
- Representación de la señal ECG con escalado automático  
4.3.2. Interacción con el sistema  
- Controles para iniciar/detener la adquisición  
- Exportación de datos a CSV o JSON  

---

### **5. Implementación del Sistema**  
5.1. **Integración de hardware y software**  
5.1.1. Conexión del hardware con el software de adquisición  
5.1.2. Configuración del microcontrolador para transmisión de datos  
5.1.3. Interfaz de comunicación con la computadora  

5.2. **Pruebas y validación**  
5.2.1. Metodología de pruebas  
- Pruebas de precisión del sensor  
- Evaluación del ruido e interferencias  
- Validación de la frecuencia de muestreo  
5.2.2. Resultados obtenidos  
- Comparación con datos de referencia  
- Evaluación de calidad de señal  
- Análisis de error en la adquisición  

---

### **6. Análisis de Resultados**  
6.1. **Análisis de los datos adquiridos**  
- Comparación con datos de referencia clínica  
- Variabilidad de señal ECG detectada  

6.2. **Comparación con datos clínicos**  
6.3. **Evaluación del rendimiento del sistema**  
6.4. **Interpretación de resultados**  
- Identificación de limitaciones en el diseño  
- Recomendaciones para optimización  

---

### **7. Discusión**  
7.1. **Limitaciones del sistema**  
- Precisión del DAC  
- Interferencias en la señal ECG  
7.2. **Posibilidades de mejora**  
- Implementación de filtros adaptativos  
- Optimización del procesamiento en tiempo real  
7.3. **Aplicaciones futuras**  
- Uso en monitoreo remoto de pacientes  
- Aplicación en dispositivos portátiles  

---

### **8. Conclusiones y Futuras Direcciones**  
8.1. Conclusiones del proyecto  
8.2. Posibles mejoras y desarrollos futuros  
8.3. Impacto potencial en la salud y tecnología  

---

### **9. Referencias**  
9.1. Bibliografía utilizada

- Fernández, J., Ramírez, P., & Gómez, L. (2018). Monitoreo remoto de señales electrocardiográficas mediante sistemas embebidos. Revista de Ingeniería Biomédica, 35(2), 45-58.

- García, M., Pérez, D., & Torres, A. (2015). Diseño e implementación de un sistema electrocardiográfico digital para la adquisición de señales ECG. Revista de Física e Ingeniería, 55(10), 123-136.

- Martínez, R., Sánchez, B., & Ortega, F. (2019). Electrocardiografía digital y su impacto en el diagnóstico de enfermedades cardiovasculares. Journal of Biomedical Research, 12(3), 200-215.

- Rodríguez, C., & López, E. (2020). Técnicas avanzadas de procesamiento de señales ECG para la detección de arritmias. Revista Electrónica de Ingeniería Médica, 27(1), 78-92.

- Mayo Clinic. (s.f.). Electrocardiograma (ECG o EKG). Recuperado el 3 de marzo de 2025, de https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983

- Departamento de Fisiología, Facultad de Medicina, UNAM. (s.f.). Fundamentos electrofisiológicos del electrocardiograma. Recuperado el 3 de marzo de 2025, de https://fisiologia.facmed.unam.mx/wp-content/uploads/2019/10/Pr%C3%A1ctica-ECG-sesi%C3%B3n-III.pdf

- Departamento de Fisiología, Facultad de Medicina, UNAM. (s.f.). *Fundamentos electrofisiológicos del electrocardiograma*. Recuperado el 3 de marzo de 2025, de [https://fisiologia.facmed.unam.mx/wp-content/uploads/2019/10/Pr%C3%A1ctica-ECG-sesi%C3%B3n-III.pdf](https://fisiologia.facmed.unam.mx/wp-content/uploads/2019/10/Pr%C3%A1ctica-ECG-sesi%C3%B3n-III.pdf)  

- Sociedad Interamericana de Cardiología. (s.f.). *Electrocardiografía básica*. Recuperado el 3 de marzo de 2025, de [https://www.siacardio.com/wp-content/uploads/2015/01/ECG-Capitulo-1-Conceptos-b-%C3%ADsicos.pdf](https://www.siacardio.com/wp-content/uploads/2015/01/ECG-Capitulo-1-Conceptos-b-%C3%ADsicos.pdf)  

- Martínez Romo, J. C., Luna Rosas, F. J., de Luna Ortega, C. A., Gómez Rosas, G., & Peña Lecona, F. G. (2008). *Reducción de ruido digital en señales ECG utilizando filtraje por convolución*. Recuperado de [https://dialnet.unirioja.es/descarga/articulo/6106127.pdf](https://dialnet.unirioja.es/descarga/articulo/6106127.pdf)

- Rodenas, J., Garcia, M., Rieta, J. J., & Alcaraz, R. (2024). *An Efficient Algorithm Based on Wavelet Transform to Reduce Powerline Noise From Electrocardiograms*. Recuperado de [https://arxiv.org/abs/2401.10694](https://arxiv.org/abs/2401.10694)

- Schiller. (2025). *Calidad de la señal en el electrocardiógrafo: Clave para diagnósticos precisos y confiables*. Recuperado de [https://schillerlatam.com/calidad-de-la-senal-en-el-electrocardiografo-clave-para-diagnosticos-precisos-y-confiables/](https://schillerlatam.com/calidad-de-la-senal-en-el-electrocardiografo-clave-para-diagnosticos-precisos-y-confiables/)

- Vázquez Seisdedos, C. R., Evangelista Neto, J., Valdés Pérez, F. E., & Limao de Oliveira, R. C. (2010). *Procesamiento y análisis del electrocardiograma (ECG) ambulatorio: problemas y soluciones*. Recuperado de [https://www.redalyc.org/pdf/1813/181317867006.pdf](https://www.redalyc.org/pdf/1813/181317867006.pdf) 

- González Murillo, J. J. (2014). *Filtrado básico de señales biomédicas*. Recuperado el 3 de marzo de 2025, de [https://www.researchgate.net/publication/271273652_Filtrado_Basico_de_Senales_Biomedicas](https://www.researchgate.net/publication/271273652_Filtrado_Basico_de_Senales_Biomedicas)  

- Ochoa, A., Maciel, M., Estrada, F., Díaz, C., Félix, R., Álvarez, J., & Vásquez, J. C. (2011). *Sistema de adquisición y procesamiento de señales electrocardiográficas*. Recuperado el 3 de marzo de 2025, de [https://www.iiisci.org/journal/pdv/risci/pdfs/NK117CZ.pdf](https://www.iiisci.org/journal/pdv/risci/pdfs/NK117CZ.pdf)  

- Vásquez, J. C., Ochoa, A., Maciel, M., Estrada, F., Díaz, C., Félix, R., & Álvarez, J. (2007). *Análisis y supervisión de la señal cardíaca utilizando herramientas de software libre*. Recuperado el 3 de marzo de 2025, de [https://dialnet.unirioja.es/descarga/articulo/4803800.pdf](https://dialnet.unirioja.es/descarga/articulo/4803800.pdf)

- Dewesoft. (s.f.). *Adquisición de datos (DAQ): la guía completa*. Recuperado el 3 de marzo de 2025, de [https://dewesoft.com/es/blog/que-es-adquisicion-de-datos](https://dewesoft.com/es/blog/que-es-adquisicion-de-datos)  

- Omega Engineering. (s.f.). *Sistema de adquisición de datos*. Recuperado el 3 de marzo de 2025, de [https://es.omega.com/prodinfo/adquisicion-de-datos.html](https://es.omega.com/prodinfo/adquisicion-de-datos.html)  

- Siemens. (s.f.). *Sistemas de adquisición de datos en simulación y pruebas*. Recuperado el 3 de marzo de 2025, de [https://plm.sw.siemens.com/es-ES/simcenter/simulation-test/data-acquisition-systems](https://plm.sw.siemens.com/es-ES/simcenter/simulation-test/data-acquisition-systems) 

9.2. Fuentes de información  
9.3. Recursos adicionales  

---

### **10. Anexos**  
10.1. Códigos fuente  
10.2. Diagramas y esquemas eléctricos  
10.3. Documentación adicional  
10.4. Resultados adicionales de pruebas  
10.5. Diagramas y gráficos  

---

### **11. Solución de Problemas**  
11.1. Errores comunes y soluciones  
- Problemas en la adquisición de datos  
- Fallos en la comunicación serial  
- Interferencias en la señal ECG  
11.2. Depuración y diagnóstico  
- Métodos de depuración en sistemas embebidos  
- Pruebas con osciloscopio y analizador lógico  
11.3. Estrategias de optimización  

