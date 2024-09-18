from pynput import keyboard
import os
import json
import subprocess
import time

import abmouse

import aareadmd
layout = aareadmd.getmdlayers('01mapping.md')

keyboard_controller = keyboard.Controller()

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
                abmouse.move_with_acceleration(0, -1)
            elif keycode == 106:  # j
               abmouse.move_with_acceleration(0, 1)
            elif keycode == 104:  # h
                abmouse.move_with_acceleration(-1, 0)
            elif keycode == 108:  # l
                abmouse.move_with_acceleration(1, 0)

            if keycode == 100: abmouse.mousepress('MCL') # d

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

        if keycode == 100: abmouse.mouserelease('MCL') # d

        # if 106 == keycode: keyboard_controller.release('a') #j

        # if key == keyboard.Key.esc:

        #     subprocess.run(['setxkbmap'], shell=True, check=True)
        #     return False  # Interrompe o listener

    except AttributeError:
        pass

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

