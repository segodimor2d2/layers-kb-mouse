import os
import json
import subprocess
import time


from pynput.keyboard import Listener, Controller as KeyboardController

# Instancia o controlador de teclado
keyboard = KeyboardController()

import ab_mouse

from ab_mouse import move_with_acceleration
from ab_mouse import mousepress
from ab_mouse import mouserelease
from ab_mouse import reset_time

from aa_readmd import getmdlayers
from aa_readmd import process_layout
from aa_readmd import dccKeycodesToPositions
from aa_readmd import getTriggersPosition


recjson = '10recKeycodes.json'
charsToKeycodes, keycodesToChars = getmdlayers(recjson)

layersfile = '01layers.md'
layers = process_layout(layersfile)

''' triggersToKeycodes dccPositionsToKeycodes'''
keycodesToPositions, positionsToKeycodes = dccKeycodesToPositions(layers, charsToKeycodes)

''' leer os trigger dos layers '''
triggers = getTriggersPosition(layers, positionsToKeycodes)

def getKeyNow(keycode, layer_active):
    positionKey = keycodesToPositions[keycode]
    newKeyOnlayer = layers[layer_active][positionKey[0]][positionKey[1]][positionKey[2]]
    return newKeyOnlayer 

pressed_keys = set()
estado = False


# Variáveis globais para armazenar a tecla e o tempo
pressed_keys = set()
current_key = None
press_time = None

# Tempo em segundos para disparar o evento
trigger_time = 2

layer_active = 1
def on_press(key):
    global cont, estado, layer_active
    global current_key, press_time

    # if not estado:
    #     subprocess.run(['./91layer0.sh'], shell=True, check=True)
    #     estado = True

    # time.sleep(0.5)
    try:
        # lee a teclas precionada
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.add(keycode)

        newKeyOnlayer = getKeyNow(keycode, layer_active)
        print(layer_active,newKeyOnlayer,keycode,pressed_keys)

        if newKeyOnlayer == 'ESC': layer_active = 1
        elif newKeyOnlayer == 'MDin': layer_active = 2
        elif newKeyOnlayer == 'MDnu': layer_active = 3
        elif newKeyOnlayer == 'MDmo': layer_active = 4

        # if layer_active == 2:
        #     keyboard.press(newKeyOnlayer)

        if charsToKeycodes['WN'] in pressed_keys and charsToKeycodes['ESC'] in pressed_keys:
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass


def on_release(key):
    global current_key, press_time
    try:
        print('-------------------------------------')
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk

        pressed_keys.discard(keycode)
        newKeyOnlayer = getKeyNow(keycode, layer_active)
        print(layer_active,newKeyOnlayer,keycode,pressed_keys)

        # print(keycode)
        # print(pressed_keys)

        # listenerLayerOn, listKeys = findIndexTrigger(triggers, pressed_keys)
        # # print(listenerLayerOn, listKeys)
        # if listKeys:
        #     for key in listKeys:
        #         if key in keycodesToPositions:
        #             positionKey = keycodesToPositions[key]
        #             newKeyOnlayer = layers[listenerLayerOn][positionKey[0]][positionKey[1]][positionKey[2]]
        #             # print(newKeyOnlayer)
        #             # if newKeyOnlayer == 'SP1':
        #             #     delay(1000)
        #             # else:
        #             #     keyboard.release(newKeyOnlayer)


    except AttributeError:
        pass

    # time.sleep(0.07)
    # print('oioioi')

with Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

