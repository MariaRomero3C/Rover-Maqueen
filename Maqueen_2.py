from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    sensor_1 = robot.read_patrol (0)
    sensor_2 = robot.read_patrol (1)
    if sensor_1 == 1 and sensor_2 == 1:
        robot.motor_stop_all()
    elif sensor_1 == 0 and sensor_2 == 1:
        robot.set_motor(0,0)
        robot.set_motor(1,255)
    elif sensor_1 == 1 and sensor_2 == 0:
        robot.set_motor(0,255)
        robot.set_motor(1,0)
    elif sensor_1 == 0 and sensor_2 == 0:
        robot.set_motor(0,50)
        robot.set_motor(1,50)    
    else:
        display.show(Image.HEART)
