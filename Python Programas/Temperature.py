from time import sleep
from machine import ADC

thermistor_pin = ADC(26)

while True:
    thermistor_value = thermistor_pin.read_u16()
    print(thermistor_value)
    sleep(0.1)