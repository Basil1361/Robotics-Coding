"""HC-SR04 Ultrasonic Ranger"""
from microbit import *
from machine import time_pulse_us

# Choose I/O pins based on wiring
trig = pin14
echo = pin15

# Setup I/O
trig.write_digital(0)
echo.read_digital()

# Continuous Ultrasonic Ranging!
while True:
    # Output a pulse to trigger ultrasonic burst
    trig.write_digital(1)
    trig.write_digital(0)

    # Measure the input echo pulse in microseconds, convert to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000

    # Calculate distance in cm and display on micro:bit
    dist_cm = (t_echo / 2) * 34300
    display.scroll(str(dist_cm))

    # Must pause between measurements (superfluous due to scroll)
    sleep(100)
