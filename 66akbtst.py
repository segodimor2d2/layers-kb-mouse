from pynput import keyboard, mouse

# Inicializar o controlador de mouse
mouse_controller = mouse.Controller()

# Funções para mover o mouse
def move_mouse(x, y):
    mouse_controller.move(x, y)

def click_mouse(button):
    mouse_controller.click(button)

# Funções de callback
def on_press(key):
    try:
        if key.char == 'k':
            move_mouse(0, -10)
        elif key.char == 'j':
            move_mouse(0, 10)
        elif key.char == 'h':
            move_mouse(-10, 0)
        elif key.char == 'l':
            move_mouse(10, 0)
        elif key.char == 'f':
            click_mouse(mouse.Button.left)
        elif key.char == 'd':
            click_mouse(mouse.Button.middle)
        elif key.char == 's':
            click_mouse(mouse.Button.right)
        return True  # Continua a escutar e não interrompe
    except AttributeError:
        pass

def on_release(key):
    # Se a tecla "esc" for pressionada, sair do listener
    if key == keyboard.Key.esc:
        return False  # Interrompe o listener

# Configurar os listeners
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
