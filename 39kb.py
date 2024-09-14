from pynput import keyboard

# 16777215 caps
# 65307 esc
# 65515 win

# Define a lista para armazenar as teclas pressionadas
pressed_keys = set()

def on_press(key):
    try:
        # Adiciona a tecla pressionada ao conjunto
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.add(keycode)
        print(pressed_keys)

    except AttributeError:
        pass

    if 65515 in pressed_keys and 16777215 in pressed_keys:  # win + caps
        print('layers')

    # Para sair do programa use win + esc
    if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
        return False

def on_release(key):
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)
    except AttributeError:
        pass

# Configura o Listener
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release

) as listener:
    listener.join()
