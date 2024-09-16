from pynput import keyboard, mouse
import os
import json
import subprocess

# 16777215 caps
# 65307 esc
# 65515 win

mouse_controller = mouse.Controller()


def move_mouse(x, y):
    mouse_controller.move(x, y)

def click_mouse(button):
    mouse_controller.click(button)

estado = False

# Define a lista para armazenar as teclas pressionadas
pressed_keys = set()
def on_press(key):
    global cont, estado
    try:
        # Adiciona a tecla pressionada ao conjunto
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        print(keycode)

        pressed_keys.add(keycode)

        # Para sair do programa use win + esc
        # if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
        if 65307 in pressed_keys:  # esc
            if not estado:
                subprocess.run(['./91layer0.sh'], shell=True, check=True)
                # subprocess.run(['./93layer2.sh'], shell=True, check=True)
                print('layers 88888888')
                estado = True

            if keycode == 107: move_mouse(0, -10) # k
            elif keycode == 106: move_mouse(0, 10) # j
            elif keycode == 104: move_mouse(-10, 0) # h
            elif keycode == 108: move_mouse(10, 0) # l
            elif keycode == 102: click_mouse(mouse.Button.left) # f
            elif keycode == 100: click_mouse(mouse.Button.middle) # d
            elif keycode == 115: click_mouse(mouse.Button.right) # s

        # if 65515 in pressed_keys and 65515 in pressed_keys:  # win + caps
        if 65515 in pressed_keys: # win
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass


def on_release(key):
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)

        # if key == keyboard.Key.esc:
        #     subprocess.run(['setxkbmap'], shell=True, check=True)
        #     return False  # Interrompe o listener

    except AttributeError:
        pass

# Configura o Listener
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

