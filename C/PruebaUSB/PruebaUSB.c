#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "hardware/adc.h"

#define UART_ID uart0
#define BAUD_RATE 9600
#define UART_TX_PIN 16
#define ADC_PIN 26
#define LED_PIN 25  // Definir el pin para el LED

int main() {
    // Inicializa el hardware
    stdio_init_all();
    uart_init(UART_ID, BAUD_RATE);
    
    // Configura el pin TX
    gpio_set_function(UART_TX_PIN, UART_FUNCSEL_NUM(UART_ID, UART_TX_PIN));
    
    // Configura el ADC
    adc_init();
    adc_gpio_init(ADC_PIN);
    adc_select_input(0); // Selecciona el canal 0 (GPIO 26)

    // Configura el pin del LED como salida
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);  // Establecer el pin como salida

    // Bucle infinito para leer el ADC y enviar datos cada 50 ms
    while (true) {
        // Lee el valor del ADC y normaliza
        float adc_value = adc_read() / 65535.0; // Normaliza el valor a [0, 1]

        // Envía el valor del ADC a través de UART
        char buffer[50];
        snprintf(buffer, sizeof(buffer), "%f\n", adc_value);
        uart_puts(UART_ID, buffer);

        // Controla el LED según el valor del ADC
        if (adc_value < 0.05) {
            gpio_put(LED_PIN, true);  // Enciende el LED
        } else {
            gpio_put(LED_PIN, false); // Apaga el LED
        }

        // Espera 50 ms
        sleep_ms(50);
    }

    return 0; // Por si acaso
}
