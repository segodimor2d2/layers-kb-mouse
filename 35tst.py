from pynput import keyboard, mouse
import subprocess

leader01 = 0
layerNum = 0

# Inicializar o controlador de mouse
mouse_controller = mouse.Controller()

# Funções para mover o mouse
def move_mouse(x, y):
    mouse_controller.move(x, y)

def click_mouse(button):
    mouse_controller.click(button)

def change_layout(layout_file):
    #subprocess.run([layout_file], check=True)
    subprocess.run([layout_file], shell=True, check=True)

def on_press(key):
    global leader01
    global layerNum

    try:
        # Obtenha o código da tecla pressionada
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        # print(f"Tecla pressionada: {key}, Keycode: {keycode}")
    except AttributeError:
        # print(f"Tecla pressionada: {key}")
        keycode = None

    if keycode == 65515:
        layerNum = leader01 % 3

        if layerNum == 0:
            print("layer normal")
            change_layout('setxkbmap')
        elif layerNum == 1:
            print("layer primeiro")
            change_layout('./layer1.sh')
        elif layerNum == 2:
            print("layer segundo")
            change_layout('./layer2.sh')

        leader01 += 1

    if keycode == 107 and layerNum == 2: # k
        move_mouse(0, -10)

    elif keycode == 106 and layerNum == 2: # j
        move_mouse(0, 10)

    elif keycode == 104 and layerNum == 2: # h
        move_mouse(-10, 0)

    elif keycode == 108 and layerNum == 2: # l
        move_mouse(10, 0)

    elif keycode == 102 and layerNum == 2: # f
        click_mouse(mouse.Button.left)

    elif keycode == 100 and layerNum == 2: # d
        click_mouse(mouse.Button.middle)

    elif keycode == 115 and layerNum == 2: # s
        click_mouse(mouse.Button.right)

    return True  # Continua a escutar e não interrompe

def on_release(key):
    # Saia do programa quando a tecla 'esc' for pressionada
    if key == keyboard.Key.esc:
        return False

# Configurar o listener para o teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

