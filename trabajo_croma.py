from microbit import *
from maqueen import *

robot = Maqueen()

display.show(1)
sleep(1300)
robot.girar_izquierda()
robot.mover_celda()
robot.mover_celda()
robot.girar_derecha()
display.show(2)
sleep(1300)
robot.girar_izquierda()
robot.mover_celda()
robot.mover_celda()
robot.girar_derecha()
display.scroll(79)
sleep(300)
robot.girar_izquierda()
robot.mover_celda()
robot.mover_celda()
robot.girar_derecha()
display.scroll(145)
