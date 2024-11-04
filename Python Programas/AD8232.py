from time import sleep
from machine import ADC

adc = ADC(26)

while True:
    print(adc.read_u16()/2**16)
    sleep(0.05)