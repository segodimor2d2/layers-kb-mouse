from pynput import keyboard

# Dicionário para mapear keycodes para nomes de teclas
keycode_map = {
    # Atualize com os keycodes obtidos
}

def on_press(key):
    try:
        # Obtenha o keycode da tecla pressionada
        keycode = key.vk if hasattr(key, 'vk') else None
        # Imprima o keycode e a tecla pressionada
        if keycode is not None:
            # Adicione uma entrada ao dicionário de keycodes
            if keycode not in keycode_map:
                keycode_map[keycode] = str(key)
            print(f"Tecla pressionada: {key}, Keycode: {keycode}")
        else:
            print(f"Tecla pressionada: {key} (Sem keycode)")
    except AttributeError:
        print(f"Tecla pressionada: {key} (Erro ao obter keycode)")

def on_release(key):
    # Saia do programa quando a tecla 'esc' for pressionada
    if key == keyboard.Key.esc:
        print("Keycodes detectados:", keycode_map)
        return False

# Configurar o listener para o teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
