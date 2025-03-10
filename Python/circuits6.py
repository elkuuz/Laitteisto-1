from machine import Pin
import time

# Define input and output pins
button = Pin(7, Pin.IN, Pin.PULL_UP)
lamp = Pin(20, Pin.OUT)

# Define states
OFF = 0
ON = 1

# Initialize state
state = OFF

# Function to debounce the button
def debounce(pin):
    time.sleep(0.05)  # Adjust the delay as needed
    return pin.value()

while True:
    if state == OFF:
        lamp.value(0)  # Ensure the lamp is off
        if debounce(button) == 0:  # Button pressed
            state = ON

    elif state == ON:
        lamp.value(1)  # Turn the lamp on
        if debounce(button) == 1:  # Button released
            while debounce(button) == 1:  # Wait for the next press
                time.sleep(0.05)
            state = OFF

    time.sleep(0.05)  # 20 Hz clock frequency (50 ms period)

