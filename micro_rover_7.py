from microbit import *
from MicroRover import *

robot = Micro_Rover()
contador = 0

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
        robot.motor(255,255)
        sleep(1200)
        break
    else:
        robot.motor(255,255)

while True:
    contador = contador + 1
    if contador == 13:
        robot.motor(0,0)
