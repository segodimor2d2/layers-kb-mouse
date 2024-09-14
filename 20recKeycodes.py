from pynput import keyboard
import os
import json

# 16777215 caps
# 65307 esc
# 65515 win

# Define a lista para armazenar as teclas pressionadas
pressed_keys = set()
dictionaryKeys = {}


def on_press(key):
    global cont
    try:
        # Adiciona a tecla pressionada ao conjunto
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.add(keycode)

    except AttributeError:
        pass

    dictionaryKeys[getKey[cont]] = list(pressed_keys)

    os.system('clear')
    txt = '\n%s = %s' % (getKey[cont], pressed_keys)
    print(txt)

    cont += 1

    if cont == len(getKey):
        print(dictionaryKeys)

        with open('11recKeycodes.json', 'w') as json_file:
            json.dump(dictionaryKeys, json_file, indent=4)

        cont = 0
        return False

    # if 65515 in pressed_keys and 16777215 in pressed_keys:  # win + caps
    #     print('layers')

    # Para sair do programa use win + esc
    if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
        return False

    print('\nPRESS ',getKey[cont])

def on_release(key):
    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        pressed_keys.discard(keycode)

        # if key == keyboard.Key.esc:
        #     return False  # Interrompe o listener

    except AttributeError:
        pass

getKey = [
    'q','a','z','w','s','x','e','d','c','r','f','v','t','g','b',
    'y','h','n','u','j','m','i','k','COMMA','o','l','PERIOD ','p','CEDILLA','SEMICOLON',
    'ACUTE ','TILDE','FORWARD ','LBRACKET ','RBRACKET','BACKSLASH',
    '1','2','3','4','5','6','7','8','9','0','HYPHEN','EQUALS',
    'ESC','TAB','SHIFTL','CTRL_L','WIN','ALT_L','SPACE',
    'ALT_R','CTRL_R','SHIFT_R','ENTER','BACK',
    'K001',
    'CAPS',
]

os.system('clear')
cont = 0
print('\nPRESS ',getKey[cont])

# Configura o Listener
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

