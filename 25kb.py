import os
import json
import subprocess
import time

from pynput import keyboard
import ab_mouse
keyboard_controller = keyboard.Controller()

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
            return idx
    return 0


pressed_keys = set()
estado = False

layer_active = 0

def on_press(key):
    global cont, estado, layer_active
    # global evntTriggeredXP = False

    if not estado:
        subprocess.run(['./91layer0.sh'], shell=True, check=True)
        estado = True

    try:
        # lee a teclas precionada
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.add(keycode)
        # print(pressed_keys)

        listenerLayerOn = findIndexTrigger(triggers, pressed_keys)
        print(listenerLayerOn)

        # if not evntTriggeredXP and listenerLayerOn > 0:
        #     layer_active = listenerLayerOn
        #     evntTriggeredXP = True
        #
        # elif evntTriggeredXP and listenerLayerOn <= 0:
        #     evntTriggeredXP = False

        # for key in pressed_keys:
        #     if not key in triggers[listenerLayerOn]:
        #         positionKey = keycodesToPositions[key]
        #         newKeyOnlayer = layers[listenerLayerOn][positionKey[0]][positionKey[1]][positionKey[2]]
        #         keyboard_controller.press(newKeyOnlayer)

        if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass


def on_release(key):

    try:
        # lee a tecla solta
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)
        # print(pressed_keys)

    except AttributeError:
        pass


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

