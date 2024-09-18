from pynput import keyboard, mouse
import os
import json
import subprocess
import time

from pynput.mouse import Button, Controller
mouse = Controller()

import aareadmd
layout = aareadmd.getmdlayers('01mapping.md')

keyboard_controller = keyboard.Controller()

estado = False
pressed_keys = set()

start_time = None
acceleration_factor = 0.5
initial_movement = 5  # Movimento inicial fixo

# Função para mover o mouse com aceleração
def move_with_acceleration(direction_x, direction_y):
    global start_time
    
    if start_time is None:
        start_time = time.time()
        # Faz o movimento inicial significativo
        mouse.move(direction_x * initial_movement, direction_y * initial_movement)
        return  # Retorna para não aplicar aceleração no primeiro movimento
    
    # Calcula o tempo que a tecla foi mantida pressionada
    elapsed_time = time.time() - start_time
    
    # Aceleração quadrática após o movimento inicial
    speed = int((elapsed_time ** 2) * acceleration_factor * 100)
    
    # Move o mouse aplicando a aceleração
    mouse.move(direction_x * speed, direction_y * speed)

# Função para resetar o tempo
def reset_time():
    global start_time
    start_time = None

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
                move_with_acceleration(0, -1)
            elif keycode == 106:  # j
                move_with_acceleration(0, 1)
            elif keycode == 104:  # h
                move_with_acceleration(-1, 0)
            elif keycode == 108:  # l
                move_with_acceleration(1, 0)

            if keycode == 100: mouse.press(Button.left) # d

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

        if keycode == 100: mouse.release(Button.left) # d

        reset_time()  # Reseta o tempo ao soltar a tecla

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

