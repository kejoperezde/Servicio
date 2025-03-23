#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <termios.h>
#include <time.h>

#define SERIAL_PORT "/dev/rfcomm0"  // Cambia esto según tu configuración
// #define SERIAL_PORT "/dev/ttyUSB0"  // Cambia esto según tu configuración
#define TIMEOUT 10  // Tiempo en segundos durante el cual leeremos datos

// Función para configurar el puerto serie
int setup_serial_port(const char *port) {
    int fd = open(port, O_RDWR | O_NOCTTY | O_NDELAY);
    if (fd == -1) {
        perror("No se pudo abrir el puerto serie");
        return -1;
    }

    struct termios options;
    tcgetattr(fd, &options);
    
    // Configurar puerto serie
    options.c_cflag = B9600 | CS8 | CLOCAL | CREAD;  // 9600 baudios, 8 bits de datos, sin paridad
    options.c_iflag = IGNPAR;  // Ignorar errores de paridad
    options.c_oflag = 0;  // Sin modificación del flujo de salida
    options.c_lflag = ICANON;  // Modo de entrada canónica

    // Aplicar configuración
    tcsetattr(fd, TCSANOW, &options);

    return fd;
}

// Función para enviar un "1" o "0" por el puerto serie
void send_data(int fd, const char *data) {
    write(fd, data, strlen(data));  // Enviar datos por el puerto serie
}

int main() {
    int fd = setup_serial_port(SERIAL_PORT);
    if (fd == -1) {
        return 1;  // Error al abrir el puerto
    }

    char buffer[256];  // Buffer para almacenar los datos recibidos
    int bytes_read;
    int count = 0;  // Contador para contar cuántas veces se reciben datos
    time_t start_time = time(NULL);
    
    printf("Esperando datos durante 10 segundos...\n");

    // Enviar un "1" por el puerto serie
    send_data(fd, "1");

    // Leer datos durante n segundos
    while (time(NULL) - start_time < TIMEOUT) {
    // while (count < 1912) {
        bytes_read = read(fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            buffer[bytes_read] = '\0';  // Asegurarse de que la cadena esté terminada en '\0'
            // printf("Dato recibido: %s\n", buffer);
            count++;  // Incrementar el contador cada vez que se recibe algo
        }
        // usleep(100000);  // Dormir durante 100 ms para evitar que el CPU esté en uso continuo
    }

    // Enviar un "1" por el puerto serie
    send_data(fd, "0");
    close(fd);

    printf("Se recibieron datos %d veces durante %d segundos.\n", count, TIMEOUT);
    printf("Tiempo de lectura completado.\n");

    return 0;
}
