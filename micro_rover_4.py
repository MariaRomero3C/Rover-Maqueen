
from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    sensor = robot.infrared_sensor_value()
    display.show(sensor)
