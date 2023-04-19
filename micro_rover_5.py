from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(0,0)
        sleep(500)
    else:
        robot.motor(255,255)
