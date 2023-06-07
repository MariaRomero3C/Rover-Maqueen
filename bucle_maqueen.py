# Imports go at the top
from microbit import *
from maqueen import *

robot = Maqueen()

x = 0

while x<4:
    robot.mover_celda()
    sleep(510)
    robot.girar_derecha()
    x = x + 1
