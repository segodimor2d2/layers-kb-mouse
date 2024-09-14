from pynput import keyboard, mouse
import subprocess

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
        self.kwin = False
        self.kcaps = False
        self.kesc = False

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
            # print(f"Tecla pressionada: {key}, Keycode: {keycode}")
        except AttributeError:
            keycode = None

        if keycode == 65515: self.kwin = True # Win key
        if keycode == 65509: self.kcaps = True # Caps Lock key
        if keycode == 65307: self.kesc = True # esc

        if self.kwin and self.kcaps:
            print('Win + Caps Lock pressionados ao mesmo tempo')
            # Execute a ação desejada aqui

    def on_release(self, key):
        try:
            keycode = key.vk if hasattr(key, 'vk') else key.value.vk
            # print(f"Tecla liberada: {key}, Keycode: {keycode}")
        except AttributeError:
            keycode = None

        if keycode == 65515: self.kwin = False # Win key
        if keycode == 65509: self.kcaps = False # Caps Lock key
        if keycode == 65307: self.kesc = True # esc 

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
