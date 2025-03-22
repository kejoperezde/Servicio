#include <stdio.h>
#include "hardware/uart.h"
#include "hardware/adc.h"

#define UART_ID uart0
#define BAUD_RATE 9600  // Velocidad de baudios para UART
#define UART_TX_PIN 16  // Pin TX para UART
#define UART_RX_PIN 17  // Pin RX para UART
#define LED_PIN 25  // Pin del LED
#define ADC_PIN 26  // Pin del ADC (GPIO 26)

// Variable para controlar el estado de envío de datos
bool sending_data = false;

int main() {
    // Inicializa el hardware
    
    // Configura el UART
    uart_init(UART_ID, BAUD_RATE);  // Configura la UART
    gpio_set_function(UART_TX_PIN, GPIO_FUNC_UART);  // Configura el pin TX para UART
    gpio_set_function(UART_RX_PIN, GPIO_FUNC_UART);  // Configura el pin RX para UART
    
    // Configura el ADC
    adc_init();
    adc_gpio_init(ADC_PIN);  // Configura el pin GPIO 26 como entrada para el ADC
    adc_select_input(0);  // Selecciona el canal 0 (GPIO 26)
    
    // Configura el pin del LED (GPIO 25)
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);  // Configura el pin del LED como salida
    gpio_put(LED_PIN, 0);  // Configurar el led en estado apagado
    
    char received_char;
    
    // Bucle principal
    while (true) {
        // Lee un byte de datos desde UART (Bluetooth)
        if (uart_is_readable(UART_ID)) {
            received_char = uart_getc(UART_ID);  // Obtiene el carácter recibido

            // Si recibimos '1', comenzamos a enviar datos del ADC
            if (received_char == '1') {
                sending_data = true;  // Activar el envío de datos
                gpio_put(LED_PIN, 1);  // Enciende el LED para indicar que estamos enviando
            }
            
            // Si recibimos '0', dejamos de enviar datos del ADC
            if (received_char == '0') {
                sending_data = false;  // Detener el envío de datos
                gpio_put(LED_PIN, 0);  // Apaga el LED para indicar que hemos detenido el envío
            }
        }

        // Si estamos enviando datos, lee el valor del ADC y envíalo por UART
        if (sending_data) {
            uint16_t adc_value = adc_read();  // Lee el valor del ADC (0-4095)
            
            // Formatea el valor del ADC como cadena y lo envía por UART
            char buffer[10];
            snprintf(buffer, sizeof(buffer), "%u\n", adc_value);  // Formato como entero sin signo

            uart_puts(UART_ID, buffer);  // Envía el valor del ADC

        }
    }

}