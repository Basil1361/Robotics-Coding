from microbit import *

ip1 = pin2
ip2 = pin1

while True:
    sv = ip1.read_analog()
    display.scroll(sv)
    sleep(100)
    sv2 = ip2.read_analog()
    display.scroll(sv2)
