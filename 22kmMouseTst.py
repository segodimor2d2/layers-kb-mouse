from pynput import keyboard, mouse
import os
import json
import subprocess

# 16777215 caps
# 65307 esc
# 65515 win

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

def move_mouse(x, y):
    mouse_controller.move(x, y)

def click_mouse(button):
    mouse_controller.click(button)

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

        if 100 in pressed_keys and 102 in pressed_keys: #df

            if keycode == 107: move_mouse(0, -10) # k
            elif keycode == 106: move_mouse(0, 10) # j
            elif keycode == 104: move_mouse(-10, 0) # h
            elif keycode == 108: move_mouse(10, 0) # l
            # elif keycode == 102: click_mouse(mouse.Button.left) # f
            # elif keycode == 100: click_mouse(mouse.Button.middle) # d
            # elif keycode == 115: click_mouse(mouse.Button.right) # s

        if 106 == keycode: keyboard_controller.press('a') #j

        if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass


def on_release(key):
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)

        if 106 == keycode: keyboard_controller.release('a') #j

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

