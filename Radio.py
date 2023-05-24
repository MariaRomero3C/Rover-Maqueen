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
radio.config(channel=18, group=0)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('vuelta')
        display.show(Image.HAPPY)  
        sleep(100)
    elif button_a.is_pressed():
        radio.send('izquierda')
        display.show(Image.ARROW_W)  
        sleep(100)
    elif button_b.is_pressed():
        radio.send('derecha')
        display.show(Image.ARROW_E)  
        sleep(100)
    else:
        display.clear()  
    sleep(100)
