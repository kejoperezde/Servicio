import time
from machine import Pin

p25 = Pin(25,Pin.OUT)

while True:
    p25.on()
    time.sleep_ms(800)
    p25.off()
    time.sleep_ms(800)