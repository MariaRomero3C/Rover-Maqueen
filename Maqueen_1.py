from microbit import *
from Maqueen import *

robot = Maqueen()

while True:
    sensor_1 = robot.read_patrol(0)
    sensor_2 = robot.read_patrol(1)

    if button_a.is_pressed():
        display.show(str(sensor_1))
    elif button_b.is_pressed():
        display.show(str(sensor_2))
