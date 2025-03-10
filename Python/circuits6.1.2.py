from machine import Pin
import time

# Define pins
button = Pin(7, Pin.IN, Pin.PULL_UP)
alarm = Pin(9, Pin.IN, Pin.PULL_UP)
red_light = Pin(22, Pin.OUT)
siren = Pin(20, Pin.OUT)

# Define states
S0 = 0
S1 = 1
S2 = 2
S3 = 3

# Initial state
state = S0

while True:
    if state == S0:
        red_light.value(0)
        siren.value(0)
        if alarm.value() == 0:
            state = S1

    elif state == S1:
        red_light.value(1)
        siren.value(1)
        if button.value() == 0:
            state = S2

    elif state == S2:
        siren.value(0)
        while alarm.value() == 0:
            red_light.value(not red_light.value())
            time.sleep(0.5)
            if button.value() == 0:
                break
        if alarm.value() == 1:
            state = S3

    elif state == S3:
        red_light.value(1)
        if button.value() == 0:
            state = S0

    time.sleep(0.1)
