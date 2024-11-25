#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "hardware/adc.h"
#include "hardware/timer.h"

#define UART_ID uart0
#define BAUD_RATE 9600    // Velocidad de baudios para Bluetooth
#define UART_TX_PIN 16      // Pin TX del Bluetooth (se conecta a RX del HC-05)
#define UART_RX_PIN 17      // Pin RX del Bluetooth (se conecta a TX del HC-05)
#define ADC_PIN 26          // Pin de lectura del AD8231 (conectado al canal ADC0, A0)

// Función para inicializar el UART (Bluetooth) y el ADC
void init_uart_and_adc() {
    uart_init(UART_ID, BAUD_RATE);  // Inicializa UART con la velocidad de baudios
    gpio_set_function(UART_TX_PIN, GPIO_FUNC_UART);  // Configura el pin TX como UART
    gpio_set_function(UART_RX_PIN, GPIO_FUNC_UART);  // Configura el pin RX como UART
    adc_init();                      // Inicializa el ADC
    adc_gpio_init(ADC_PIN);          // Configura el pin ADC_PIN (GPIO 26)
    adc_select_input(0);             // Selecciona el canal ADC 0 (A0)
}

int main() {
    stdio_init_all();
    init_uart_and_adc();  // Inicializa UART y ADC

    char command_buffer[10]; // Buffer para recibir el comando desde la PC
    bool sending_data = false;
    uint32_t start_time = 0;
    
    // Bucle principal
    while (true) {
        // Si hay datos disponibles para leer en la UART (Bluetooth)
        if (uart_is_readable(UART_ID)) {
            // Lee el comando enviado desde la computadora
            uart_read_blocking(UART_ID, (uint8_t *)command_buffer, sizeof(command_buffer) - 1);
            command_buffer[sizeof(command_buffer) - 1] = '\0'; // Asegura que el comando esté terminado en nulo

            // Verifica si el comando recibido es "start"
            if (strcmp(command_buffer, "start") == 0) {
                sending_data = true;  // Comienza a enviar datos
                start_time = to_ms_since_boot(get_absolute_time());  // Toma el tiempo de inicio
            }
        }
        
        

        // Si no estamos enviando datos, seguimos esperando por nuevos comandos
        sleep_ms(100);  // Espera un poco para no sobrecargar el microcontrolador
    }

    return 0;  // Por si acaso
}
