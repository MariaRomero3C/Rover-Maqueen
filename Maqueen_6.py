# Imports go at the top
from microbit import *
from Maqueen import *

robot = Maqueen()

sensor_1 = robot.read_patrol (0)
sensor_2 = robot.read_patrol (1)

while True:
    sensor_1 = robot.read_patrol (0)
    sensor_2 = robot.read_patrol (1)
    if sensor_1 == 0 and sensor_2 == 0:
        robot.set_motor(0,80)
        robot.set_motor(1,80) 
    elif sensor_1 == 1 and sensor_2 == 0:
        robot.set_motor(0,150)
        robot.set_motor(1,0)
    elif sensor_1 == 0 and sensor_2 == 1:
        robot.set_motor(0,0)
        robot.set_motor(1,150)
    elif sensor_1 == 1 and sensor_2 == 1:
        robot.set_motor(0,80)
        robot.set_motor(1,80)    
    else:
        display.show(Image.HEART)
