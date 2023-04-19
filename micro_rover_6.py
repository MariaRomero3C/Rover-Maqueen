
from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(0,255)
        sleep(650)
        robot.motor(255,255)
        sleep(650)
        robot.motor(255,0)
        sleep(650)
        robot.motor(255,255)
        sleep(850)
        robot.motor(255,0)
        sleep(650)
        robot.motor(255,255)
        sleep(650)
        robot.motor(0,255)
        sleep(650)
    else:
        robot.motor(255,255)
