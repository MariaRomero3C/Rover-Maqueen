# Imports go at the top
from microbit import *
from maqueen import *

robot = Maqueen()

x = 0

while x<1:
    robot.forward()
    microbit.sleep(500)
    robot.motor_stop_all()
    x = x + 1
