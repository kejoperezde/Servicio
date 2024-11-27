#include <stdio.h>
#include "hardware/uart.h"
#include "hardware/adc.h"
#include "hardware/dma.h"
#include "pico/stdlib.h"

#define UART_ID uart0
#define BAUD_RATE 9600  // Velocidad de baudios para UART
#define UART_TX_PIN 16  // Pin TX para UART
#define UART_RX_PIN 17  // Pin RX para UART
#define LED_PIN 25  // Pin del LED
#define ADC_PIN 26  // Pin del ADC (GPIO 26)
#define BUFFER_SIZE 6  // Tamaño del buffer para cada valor formateado

// Variable para controlar el estado de envío de datos
bool sending_data = false;

// Buffers para DMA
uint16_t adc_value = 0;  // Para almacenar el valor del ADC
char uart_buffer[BUFFER_SIZE]; // Buffer para almacenar el valor formateado para UART

// Canal DMA
int dma_channel_adc;
int dma_channel_uart;

// Canal DMA ADC para leer datos del ADC
void setup_dma_adc_transfer() {
    // Configura el DMA para la lectura del ADC
    dma_channel_config dma_config_adc = dma_channel_get_default_config(dma_channel_adc);
    channel_config_set_transfer_data_size(&dma_config_adc, DMA_SIZE_16);  // 16 bits (valor ADC)
    channel_config_set_read_increment(&dma_config_adc, false);  // No incrementar dirección de lectura
    channel_config_set_write_increment(&dma_config_adc, false);  // Dirección de escritura fija
    channel_config_set_dreq(&dma_config_adc, DREQ_ADC);  // Fuente de DMA es el ADC

    dma_channel_configure(
        dma_channel_adc,         // Canal DMA a configurar
        &dma_config_adc,         // Configuración del canal DMA
        &adc_value,              // Dirección de escritura (almacenar el valor del ADC)
        &adc_hw->fifo,           // Dirección de lectura (FIFO del ADC)
        1,                       // Solo una transferencia (un valor del ADC)
        false                    // No iniciar automáticamente
    );
}

// Canal DMA UART para enviar datos
void setup_dma_uart_transfer() {
    // Formatea el valor del ADC en el buffer para UART
    snprintf(uart_buffer, BUFFER_SIZE, "%u\n", adc_value);  // Formato como entero sin signo

    // Configura el DMA para enviar los datos por UART
    dma_channel_config uart_dma_config = dma_channel_get_default_config(dma_channel_uart);
    channel_config_set_transfer_data_size(&uart_dma_config, DMA_SIZE_8);  // 8 bits (1 byte por carácter)
    channel_config_set_read_increment(&uart_dma_config, true);  // Incrementar dirección de lectura
    channel_config_set_write_increment(&uart_dma_config, false);  // Dirección de escritura fija (UART FIFO)
    channel_config_set_dreq(&uart_dma_config, DREQ_UART0_TX);  // Solicitar la transmisión UART

    dma_channel_configure(
        dma_channel_uart,    // Canal DMA para UART
        &uart_dma_config,    // Configuración del canal DMA
        &uart0_hw->dr,       // Dirección de escritura (registro de transmisión UART)
        uart_buffer,         // Dirección de lectura (buffer con los datos formateados)
        BUFFER_SIZE,         // Número de transferencias (tamaño del buffer UART)
        false                // No iniciar automáticamente
    );

    // Iniciar la transferencia DMA para UART
    dma_channel_start(dma_channel_uart);
}

int main() {
    // Inicializa el hardware
    stdio_init_all();
    
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
    
    // Inicialización de DMA para UART
    dma_channel_uart = dma_claim_unused_channel(true);  // Reclama un canal DMA libre para UART

    // Inicialización de DMA para ADC
    dma_channel_adc = dma_claim_unused_channel(true);  // Reclama un canal DMA libre para ADC

    // Configura el DMA para el ADC
    setup_dma_adc_transfer();

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

        // Si estamos enviando datos, leemos y enviamos el valor del ADC cada vez
        if (sending_data) {
            // Iniciar el DMA para leer el valor del ADC
            dma_channel_start(dma_channel_adc);

            // Esperamos a que el DMA termine de leer el valor del ADC
            while (dma_channel_is_busy(dma_channel_adc)) {
                tight_loop_contents();  // No hacer nada mientras el DMA está ocupado
            }

            // Después de la lectura del ADC, formateamos y enviamos el valor
            setup_dma_uart_transfer();
        }
    }
}
