import time
from machine import ADC, UART

# Inicializar el ADC y la UART
adc = ADC(26)
uart=UART(0,9600)

def enviar_datos():
    
    while True:
        medicion = adc.read_u16() / 65535  # Normaliza el valor
        ##print(f"{medicion:.4f}")
        uart.write(str(medicion))
        time.sleep(0.01)  # Espera un momento antes de la siguiente medición

# Main
if __name__ == '__main__':
    enviar_datos()
