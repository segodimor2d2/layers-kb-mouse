from pynput import keyboard, mouse
import subprocess

leader01 = 0
layerNum = 0

# Inicializar o controlador de mouse
mouse_controller = mouse.Controller()

subprocess.run(['./93layer2.sh'], shell=True, check=True)

# Funções para mover o mouse
def move_mouse(x, y):
    mouse_controller.move(x, y)

def click_mouse(button):
    mouse_controller.click(button)

def on_press(key):

    try:
        # Obtenha o código da tecla pressionada
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        # print(f"Tecla pressionada: {key}, Keycode: {keycode}")
    except AttributeError:
        # print(f"Tecla pressionada: {key}")
        keycode = None

    if keycode == 107: # k
        move_mouse(0, -10)

    elif keycode == 106: # j
        move_mouse(0, 10)

    elif keycode == 104: # h
        move_mouse(-10, 0)

    elif keycode == 108: # l
        move_mouse(10, 0)

    elif keycode == 102: # f
        click_mouse(mouse.Button.left)

    elif keycode == 100: # d
        click_mouse(mouse.Button.middle)

    elif keycode == 115: # s
        click_mouse(mouse.Button.right)

    return True  # Continua a escutar e não interrompe

def on_release(key):
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk

        if key == keyboard.Key.esc:
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False  # Interrompe o listener

    except AttributeError:
        pass

# Configura o Listener
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()


