# Imports go at the top
from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    if button_a.get_presses():
        robot.mover_celda()
    elif button_b.get_presses():
        robot.mover_celda()
        robot.mover_celda()
    else:
        display.show(Image.HEART)
