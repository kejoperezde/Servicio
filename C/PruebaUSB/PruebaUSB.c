#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"

#define UART_ID uart0
#define BAUD_RATE 115200
#define UART_TX_PIN 16

int main() {
    // Configura el UART con la velocidad requerida.
    uart_init(UART_ID, BAUD_RATE);

    // Configura el pin TX
    gpio_set_function(UART_TX_PIN, UART_FUNCSEL_NUM(UART_ID, UART_TX_PIN));

    // Bucle infinito para enviar datos cada segundo
    while (true) {
        // Envía un carácter
        uart_putc_raw(UART_ID, 'A');

        // Envía un carácter con conversiones CR/LF
        uart_putc(UART_ID, 'B');

        // Envía una cadena con conversiones CR/LF
        uart_puts(UART_ID, " Hello, UART!\n");

        // Espera 1000 ms (1 segundo)
        sleep_ms(1000);
    }

    return 0; // Por si acaso
}
