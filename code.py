
import time
from adafruit_macropad import MacroPad

macropad = MacroPad()
ultimaPosicionEncoder = 0
while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        print("K{}".format(key_event.key_number))

    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        print("*")

    position = macropad.encoder
    if position != ultimaPosicionEncoder:
        if(position>ultimaPosicionEncoder):
            print("+")
        else:
            print("-")
        ultimaPosicionEncoder = position
    time.sleep(0.001)

