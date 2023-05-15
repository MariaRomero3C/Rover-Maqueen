from microbit import *
from maqueen import *

robot = Maqueen()


while True:
    distancia = robot.read_distance()
    if distancia <= 10:
        robot.turn_left()
        robot.forward()
        sleep(500)
        robot.turn_right()
        robot.forward()
        sleep(1000)
        robot.turn_right()
        robot.forward()
        sleep(500)
        robot.turn_left()
        robot.forward()
    else:
        robot.forward()
