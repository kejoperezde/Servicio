from machine import UART, Pin
import time

# Configurar UART (por defecto UART0 en la Pico)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Enviar datos
while True:
    uart.write("Hola desde Raspberry Pi Pico!\n")
    time.sleep(1)  # Espera 1 segundo antes de enviar de nuevo
