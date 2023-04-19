from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    display.scroll(distancia)
