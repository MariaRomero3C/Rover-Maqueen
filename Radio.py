from microbit import *
import radio

# Definir imágenes de flechas
left_arrow = Image("00900:"
                   "09090:"
                   "90009:"
                   "00900:"
                   "00900")

right_arrow = Image("00900:"
                    "00900:"
                    "90009:"
                    "09090:"
                    "00900")

up_arrow = Image("00900:"
                 "09090:"
                 "90009:"
                 "00900:"
                 "00900")

radio.on()
radio.config(channel=12, group=0)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('vuelta')
        display.show(Image.HAPPY)  # Muestra la flecha hacia arriba
        sleep(100)
    elif button_a.is_pressed():
        radio.send('forward')
        display.show(Image.ARROW_N)  # Muestra la flecha hacia la izquierda
        sleep(100)
    elif button_b.is_pressed():
        radio.send('backwards')
        display.show(Image.ARROW_S)  # Muestra la flecha hacia la derecha
        sleep(100)
    else:
        display.clear()  # Limpia la pantalla si no se presiona ningún botón
    sleep(100)
