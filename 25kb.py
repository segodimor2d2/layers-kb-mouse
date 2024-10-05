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


'''
import ipdb; ipdb.set_trace()
# teste validando a key 117
positionKey = keycodesToPositions[117]
# teste pegando a key 117 do layer 1
newKeyOnlayer = layers[1][positionKey[0]][positionKey[1]][positionKey[2]]
'''

''' OS TRIGGERS NÃO SE PODEM REPETIR NOS LAYOUT '''
def findIndexTrigger(triggers, pressed_keys):
    for idx, trigger in enumerate(triggers):
        if trigger and trigger.issubset(pressed_keys):
            extras = list(pressed_keys - trigger)
            return idx, extras
    return 0, list(pressed_keys)

pressed_keys = set()
estado = False

layer_active = 0

current_key = None

def on_press(key):
    global cont, estado, layer_active
    global current_key

    # if not estado:
    #     subprocess.run(['./91layer0.sh'], shell=True, check=True)
    #     estado = True

    # time.sleep(0.5)
    try:
        # lee a teclas precionada
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        if keycode != current_key:
            current_key = keycode
            pressed_keys.add(keycode)
            print(keycode,pressed_keys)
            time.sleep(0.3)
            print(keycode,pressed_keys)

            listenerLayerOn, listKeys = findIndexTrigger(triggers, pressed_keys)
            # print(listenerLayerOn, listKeys)
            if listKeys:
                for key in listKeys:
                    if key in keycodesToPositions:
                        positionKey = keycodesToPositions[key]
                        newKeyOnlayer = layers[listenerLayerOn][positionKey[0]][positionKey[1]][positionKey[2]]
                        # print(newKeyOnlayer,keycode,pressed_keys)
                        # if newKeyOnlayer == 'SP1':
                        #     delay(5000)
                        #     print('oioioi')
                        # print(newKeyOnlayer,keycode,pressed_keys)
                        # else:
                        #     keyboard.press(newKeyOnlayer)

        if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass


def on_release(key):
    global current_key
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        if keycode == current_key:
            current_key = None
            print('-------------------------------------')
            # print(keycode)
            # print(pressed_keys)

            listenerLayerOn, listKeys = findIndexTrigger(triggers, pressed_keys)
            # print(listenerLayerOn, listKeys)
            if listKeys:
                for key in listKeys:
                    if key in keycodesToPositions:
                        positionKey = keycodesToPositions[key]
                        newKeyOnlayer = layers[listenerLayerOn][positionKey[0]][positionKey[1]][positionKey[2]]
                        # print(newKeyOnlayer)
                        # if newKeyOnlayer == 'SP1':
                        #     delay(1000)
                        # else:
                        #     keyboard.release(newKeyOnlayer)

        pressed_keys.discard(keycode)

    except AttributeError:
        pass

    # time.sleep(0.07)
    # print('oioioi')

with Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

