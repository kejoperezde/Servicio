const int sensorPin = A0; // El pin analógico al que está conectado el sensor
int sensorValue = 0; // Variable para almacenar el valor del sensor

void setup() {
    Serial.begin(9600); // Inicializa la comunicación serial a 9600 baudios
}

void loop() {
    sensorValue = analogRead(sensorPin); // Lee el valor del sensor
    String color = determineColor(sensorValue); // Determina el color basado en el valor del sensor
    Serial.print("Valor del Sensor: ");
    Serial.print(sensorValue);
    Serial.print(" - Color: ");
    Serial.println(color); // Imprime el color en el Monitor Serial
    delay(100); // Espera 100 milisegundos antes de volver a leer el sensor
}

String determineColor(int value) {
    // Mapea el valor del sensor (0-1023) a un rango de longitud de onda en nanómetros
    int wavelength = map(value, 0, 1023, 380, 750); // Mapeo de 380 nm (violeta) a 750 nm (rojo)

    // Determina el color basado en la longitud de onda
    if (wavelength >= 575 && wavelength <= 585) {
        return "Amarillo";
    } else if (wavelength >= 569 && wavelength < 579) {
        return "Verde";
    } else if (wavelength >= 570 && wavelength < 575) {
        return "Azul";
    } else if (wavelength >= 380 && wavelength < 450) {
        return "Violeta";
    } else if (wavelength >= 590 && wavelength <= 620) {
        return "Naranja";
    } else if (wavelength >= 620 && wavelength <= 750) {
        return "Rojo";
    } else {
        return "Desconocido"; // Para valores fuera del rango definido
    }
}
