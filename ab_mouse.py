import time
from pynput.mouse import Button, Controller

mouse = Controller()

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

def mousepress(button):
    if button == 'MCL': mouse.press(Button.left)
    if button == 'MCR': mouse.press(Button.right)
    if button == 'MCM': mouse.press(Button.middle)

def mouserelease(button):
    if button == 'MCL': mouse.release(Button.left)
    if button == 'MCR': mouse.release(Button.right)
    if button == 'MCM': mouse.release(Button.middle)


