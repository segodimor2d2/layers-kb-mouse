from pynput import keyboard, mouse
import subprocess
import time

class KeyboardMouseController:
    def __init__(self):
        self.leader01 = 0
        self.layerNum = 0
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
        self.key_mappings = {
            107: lambda: self.move_mouse(0, -10),  # k
            106: lambda: self.move_mouse(0, 10),   # j
            104: lambda: self.move_mouse(-10, 0),  # h
            108: lambda: self.move_mouse(10, 0),   # l
            102: lambda: self.click_mouse(mouse.Button.left),  # f
            100: lambda: self.click_mouse(mouse.Button.middle), # d
            115: lambda: self.click_mouse(mouse.Button.right)  # s
        }
        self.kwin_time = 0
        self.kcaps_time = 0
        self.threshold = 0.5  # 100ms

    def move_mouse(self, x, y):
        self.mouse_controller.move(x, y)

    def click_mouse(self, button):
        self.mouse_controller.click(button)

    def change_layout(self):
        if self.layerNum == 0:
            print("layer 0")
            subprocess.run(['setxkbmap'], shell=True, check=True)
        elif self.layerNum == 1:
            print("layer 1")
            subprocess.run(['./layer0.sh'], shell=True, check=True)
        elif self.layerNum == 2:
            print("layer 2")
            subprocess.run(['setxkbmap'], shell=True, check=True)

    def on_press(self, key):
        try:
            keycode = key.vk if hasattr(key, 'vk') else key.value.vk
            print(f"Tecla pressionada: {key}, Keycode: {keycode}")
        except AttributeError:
            keycode = None

        if keycode == 65515:  # Win key
            self.kwin_time = time.time()
        if keycode == 16777215:  # Caps Lock key
            self.kcaps_time = time.time()

        # Verifica se ambas as teclas foram pressionadas dentro do intervalo de tempo especificado
        if abs(self.kwin_time - self.kcaps_time) <= self.threshold:
            print('Win + Caps Lock pressionados ao mesmo tempo')
            # Execute a ação desejada aqui

    def on_release(self, key):
        try:
            keycode = key.vk if hasattr(key, 'vk') else key.value.vk
            # print(f"Tecla liberada: {key}, Keycode: {keycode}")
        except AttributeError:
            keycode = None

        # Reset tempos na liberação das teclas
        if keycode == 65515:  # Win key
            self.kwin_time = 0
        if keycode == 16777215:  # Caps Lock key
            self.kcaps_time = 0

        if keycode == 65307:  # Esc
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    def start(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()

if __name__ == "__main__":
    controller = KeyboardMouseController()
    controller.start()
