import os
import json
import subprocess
import time

# from pynput import keyboard
# import ab_mouse
# keyboard_controller = keyboard.Controller()

from aa_readmd import getmdlayers
from aa_readmd import process_layout
from aa_readmd import dccKeycodesToPositions

recjson = '10recKeycodes.json'
charsToKeycodes, keycodesToChars = getmdlayers(recjson)

layersfile = '01layers.md'
layers = process_layout(layersfile)

keycodesToPositions = dccKeycodesToPositions(layers, charsToKeycodes)

'''
pk = keycodesToPositions[117]
ver = layers[1][pk[0]][pk[1]][pk[2]]
import ipdb; ipdb.set_trace()
'''

estado = False
pressed_keys = set()

def on_press(key):
    global cont, estado

    if not estado:
        subprocess.run(['./91layer0.sh'], shell=True, check=True)
        estado = True

    try:
        # Adiciona a tecla pressionada ao conjunto
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.add(keycode)
        print(pressed_keys)

        if 102 in pressed_keys and 32 in pressed_keys: #FSP

            if keycode == 107:  # k
                ab_mouse.move_with_acceleration(0, -1)
            elif keycode == 106:  # j
                ab_mouse.move_with_acceleration(0, 1)
            elif keycode == 104:  # h
                ab_mouse.move_with_acceleration(-1, 0)
            elif keycode == 108:  # l
                ab_mouse.move_with_acceleration(1, 0)

            if keycode == 100: ab_mouse.mousepress('MCL') # d
            if keycode == 115: ab_mouse.mousepress('MCM') # s
            if keycode == 97: ab_mouse.mousepress('MCR') # a

            # elif keycode == 100: click_mouse(mouse.Button.middle) # d
            # elif keycode == 115: click_mouse(mouse.Button.right) # s

        #if 106 == keycode: keyboard_controller.press('a') #j

        if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass

def on_release(key):
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)

        if keycode == 100: ab_mouse.mouserelease('MCL') # d
        if keycode == 115: ab_mouse.mouserelease('MCM') # s
        if keycode == 97: ab_mouse.mouserelease('MCR') # a

        # if 106 == keycode: keyboard_controller.release('a') #j

        # if key == keyboard.Key.esc:

        #     subprocess.run(['setxkbmap'], shell=True, check=True)
        #     return False  # Interrompe o listener

        ab_mouse.reset_time()

    except AttributeError:
        pass


# with keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release
# ) as listener:
#     listener.join()

