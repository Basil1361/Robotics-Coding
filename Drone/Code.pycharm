from codrone_edu.drone import *
from random import randint
random_color = randint(1, 2)
random_delay = randint(1, 4)

def check_buttons():
    if drone.l1_pressed():
        drone.takeoff()
        print("takeoff")
    if drone.l2_pressed():
        drone.land()
        drone.close()
        print("Land")
    elif drone.r1_pressed():
        drone.flip("front")
        print("flip_Clockwise")
    elif drone.r2_pressed():
        drone.flip("back")
        print("flip_Anticlockwise")
    elif drone.p_pressed():
        drone.set_drone_LED(5,4, 50,100)
    elif drone.s_pressed():
        drone.drone_buzzer(5,5)
drone = Drone()
drone.pair()
while True:
    check_buttons()
    pitch = drone.get_left_joystick_y()
    roll = drone.get_left_joystick_x()
    throttle = drone.get_right_joystick_y()
    yaw = drone.get_right_joystick_x()
    if pitch > 60:
        pitch = 60
    if pitch < -60:
        pitch = -60
    if roll > 60:
        roll = 60
    if roll < -60:
        roll = -60
    if throttle > 60:
        throttle = 60
    if throttle < -60:
        throttle = -60
    if yaw > 60:
        yaw = 60
    if yaw < -60:
        yaw = -60
    drone.set_pitch(pitch)
    drone.set_roll(roll)
    drone.set_throttle(throttle)
    drone.set_yaw(yaw)
    drone.move()
