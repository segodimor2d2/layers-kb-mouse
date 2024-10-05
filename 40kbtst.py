import os
import json
import subprocess
import time

from pynput.keyboard import Listener, Controller as KeyboardController, Key

# Instancia o controlador de teclado
keyboard = KeyboardController()
current_key = None

def on_press(key):
    global current_key
    try:
        # Evita loop ao não enviar o 'a' caso ele já esteja sendo pressionado
        if key != current_key:
            current_key = key
            print(111)
            keyboard.press('a')
            print(222)
            keyboard.release('a')
            print(333)

    except AttributeError:
        pass


def on_release(key):
    global current_key
    try:
        if key == current_key:
            current_key = None

    except AttributeError:
        pass


with Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
