
from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(-55,-55)
        sleep(500)
        robot.motor(0,255)
        sleep(1000)
    else:
        robot.motor(255,255)
