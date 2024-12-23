from microbit import *

# Configure pins for the sensors
left_sensor = pin1  # Left IR sensor
right_sensor = pin2  # Right IR sensor

# Threshold value to detect black (adjust based on your setup)
T1 = 600  # Modify this based on your sensors' values
T2 = 50

while True:
    # Read the sensor values
    lv = left_sensor.read_analog()
    rv = right_sensor.read_analog()

    if lv < T1 and rv < T1:
        # Both sensors detect black (on the line), move forward
        display.show("S")  # Replace with motor forward control
        # motor_left.forward()
        # motor_right.forward()
    elif lv < T1:
        # Left sensor detects black (turn left)
        display.show("L")  # Replace with motor turning logic
        # motor_left.stop()
        # motor_right.forward()
    elif rv < T1:
        # Right sensor detects black (turn right)
        display.show("R")  # Replace with motor turning logic
        # motor_left.forward()
        # motor_right.stop()
    else:
        display.show("F")
