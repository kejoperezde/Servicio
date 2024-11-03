/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

// Incluye las bibliotecas necesarias
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "hardware/adc.h"
#include "hardware/dma.h"

#define UART_ID uart0
#define BAUD_RATE 9600
#define UART_TX_PIN 16
#define ADC_PIN 26
#define LED_PIN 25  // Definir el pin para el LED

// Buffer para el valor del ADC
char adc_buffer[50];

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

    // Configuración de DMA
    int chan = dma_claim_unused_channel(true);
    dma_channel_config c = dma_channel_get_default_config(chan);
    channel_config_set_transfer_data_size(&c, DMA_SIZE_16); // Usar 16 bits para el ADC
    channel_config_set_read_increment(&c, false); // No incrementar la dirección de lectura
    channel_config_set_write_increment(&c, true); // Incrementar la dirección de escritura

    // Bucle infinito para leer el ADC y enviar datos cada 50 ms
    while (true) {
        // Lee el valor del ADC
        uint16_t adc_value = adc_read() / 65535.0; // Valor sin normalizar

        // Copia el valor leído en el buffer
        snprintf(adc_buffer, sizeof(adc_buffer), "%u\n", adc_value);

        // Configura el DMA para copiar el valor del ADC al buffer
        dma_channel_configure(
            chan,
            &c,
            adc_buffer,    // Dirección de escritura (buffer)
            &adc_value,    // Dirección de lectura (valor del ADC)
            sizeof(adc_value), // Número de transferencias
            true            // Iniciar inmediatamente
        );

        // Espera a que DMA termine
        dma_channel_wait_for_finish_blocking(chan);

        // Envía el valor del ADC a través de UART
        uart_puts(UART_ID, adc_buffer);

        // Espera 50 ms
        sleep_ms(50);
    }

    return 0; // Por si acaso
}