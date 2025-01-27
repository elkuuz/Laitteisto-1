from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(27))

led = Pin("LED", Pin.OUT)

while True:
    adc_value = adc.read_u16()

    delay = adc_value / 65535

    led.on()
    sleep(delay)
    led.off()
    sleep(delay)

