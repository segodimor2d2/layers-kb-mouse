from pynput import keyboard, mouse
import time

# Inicializa o mouse
mouse_controller = mouse.Controller()

# Definir o tempo de início e a aceleração
start_time = None
acceleration_factor = 0.05

# Função para mover o mouse com aceleração
def move_with_acceleration(direction_x, direction_y):
    global start_time
    
    if start_time is None:
        start_time = time.time()
    
    # Calcula o tempo que a tecla foi mantida pressionada
    elapsed_time = time.time() - start_time
    
    # Aceleração quadrática
    speed = int((elapsed_time ** 2) * acceleration_factor * 100)
    
    # Move o mouse aplicando a aceleração
    mouse_controller.move(direction_x * speed, direction_y * speed)

# Função para resetar o tempo
def reset_time():
    global start_time
    start_time = None

# Listener de teclado
def on_press(key):
    try:
        # Usa o código da tecla para verificar o movimento
        keycode = key.vk
        if keycode == 107:  # k
            move_with_acceleration(0, -1)
        elif keycode == 106:  # j
            move_with_acceleration(0, 1)
        elif keycode == 104:  # h
            move_with_acceleration(-1, 0)
        elif keycode == 108:  # l
            move_with_acceleration(1, 0)
    except AttributeError:
        pass

def on_release(key):
    reset_time()  # Reseta o tempo ao soltar a tecla

# Configura o listener de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

