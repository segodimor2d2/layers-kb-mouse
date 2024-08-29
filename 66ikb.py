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
        # Para teclas especiais, você pode adicionar tratamento adicional aqui
        pass

    if 65515 in pressed_keys and 16777215 in pressed_keys:  # win + caps
        print('layers')

    if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
        return False
    #65307

    # if keyboard.KeyCode.from_vk(16777215) in pressed_keys and keyboard.KeyCode.from_vk(65515) in pressed_keys:
    #     print(888888)

    # if keyboard.KeyCode.from_char('a') in pressed_keys and keyboard.KeyCode.from_char('d') in pressed_keys:
    #     print("As teclas 'a' e 'd' estão sendo pressionadas simultaneamente")
    # else:
    #     # Imprime a tecla que está sendo pressionada
    #     # print(f"Tecla pressionada: {key}")
    #     pass

def on_release(key):
    try:
        # Remove a tecla liberada do conjunto
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)
    except AttributeError:
        pass

    # Para sair do programa quando a tecla ESC é pressionada
    # if key == keyboard.Key.esc:
    #     return False

# Configura o Listener
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
