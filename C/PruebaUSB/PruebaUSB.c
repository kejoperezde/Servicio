#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "hardware/adc.h"

#define UART_ID uart0
#define BAUD_RATE 9600      // Velocidad de baudios para UART
#define UART_TX_PIN 16
#define ADC_PIN 26

int main() {
    // Inicializa el hardware
    stdio_init_all();
    uart_init(UART_ID, BAUD_RATE);
    
    // Configura el pin TX para el UART
    gpio_set_function(UART_TX_PIN, GPIO_FUNC_UART);
    
    // Configura el ADC
    adc_init();
    adc_gpio_init(ADC_PIN);
    adc_select_input(0); // Selecciona el canal 0 (GPIO 26)

    // Bucle infinito para leer el ADC y enviar los datos por Bluetooth
    while (true) {
        // Lee el valor del ADC (entero de 0 a 4095)
        uint16_t adc_value = adc_read();

        // Envía el valor del ADC como un entero por UART (Bluetooth)
        char buffer[20];
        snprintf(buffer, sizeof(buffer), "%u\n", adc_value); // Formateo como entero sin signo

        uart_puts(UART_ID, buffer);

        // Espera 1 ms para incrementar la frecuencia de muestreo
        sleep_ms(50);  // Esto asegura que tomamos 1000 muestras por segundo
    }

    return 0; // Por si acaso
}
