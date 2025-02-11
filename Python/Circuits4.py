from machine import Pin
import time

button = Pin(12, Pin.IN, Pin.PULL_UP)  # Button with pull-up resistor
leds = [Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(20, Pin.OUT)]  # LEDs in correct order
counter = 0  # Counter variable


def update_leds(value):
    """Update LEDs to display the binary representation of the value."""
    for i in range(3):
        leds[i].value((value >> i) & 1)  # Set LED state based on the bit value


while True:
    if button.value() == 0:  # Button is pressed (active-low)
        counter = (counter + 1) % 8  # Increment counter and wrap around at 8
        update_leds(counter)  # Update LEDs
        while button.value() == 0:  # Wait for button to be released
            time.sleep(0.1)  # Debounce delay
