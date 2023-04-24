# Imports go at the top
from microbit import *
from Maqueen import *

robot = Maqueen()

def andar_atras():
    robot.set_motor(0, -255)
    robot.set_motor(1, -255)

while True:
    andar_atras()
