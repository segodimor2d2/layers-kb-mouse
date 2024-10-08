https://pynput.readthedocs.io/en/latest/keyboard.html


83mm x 120mm

18.20mm x 18.20mm


---

Para calcular o tempo que uma tecla está sendo pressionada e disparar um evento após 2 segundos sem soltar a tecla, você pode ajustar seu código da seguinte forma:

1. Armazene o tempo de pressionamento da tecla quando o evento `on_press` for disparado.
2. Verifique o tempo decorrido em um loop (ou em uma chamada de função).
3. Se o tempo decorrido atingir 2 segundos e a tecla ainda estiver pressionada, dispare o evento desejado.

Aqui está como você pode adaptar seu código:

```python
import time
import subprocess
from pynput.keyboard import Listener, Controller as KeyboardController

# Instancia o controlador de teclado
keyboard = KeyboardController()

# Variáveis globais para armazenar a tecla e o tempo
pressed_keys = set()
current_key = None
press_time = None

# Tempo em segundos para disparar o evento
trigger_time = 2

def findIndexTrigger(triggers, pressed_keys):
    # Seu código de busca de gatilhos
    pass

def on_press(key):
    global current_key, press_time

    try:
        # Captura o keycode da tecla pressionada
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        
        # Se uma nova tecla for pressionada, armazene o tempo inicial
        if current_key is None:
            current_key = keycode
            press_time = time.time()
            pressed_keys.add(keycode)
            print(f'Tecla pressionada: {keycode}, tempo iniciado')

        if press_time is not None:
            # Verifica se o tempo de 2 segundos foi atingido enquanto a tecla está pressionada
            elapsed_time = time.time() - press_time
            if elapsed_time >= trigger_time:
                print(f'Tecla {keycode} pressionada por {elapsed_time:.2f} segundos')
                # Aqui você pode disparar seu evento
                # Exemplo: mover o mouse, mudar layout, etc.
                # Apenas reseta o tempo se o evento for disparado
                press_time = None

        if 65515 in pressed_keys and 65307 in pressed_keys:  # win + esc
            subprocess.run(['setxkbmap'], shell=True, check=True)
            return False

    except AttributeError:
        pass

def on_release(key):
    global current_key, press_time

    try:
        keycode = key.vk if hasattr(key, 'vk') else key.value.vk
        if keycode == current_key:
            print(f'Tecla liberada: {keycode}')
            current_key = None
            press_time = None

        pressed_keys.discard(keycode)

    except AttributeError:
        pass

with Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
```

### O que foi alterado:
- Armazenamos o tempo da tecla pressionada com `press_time` e verificamos se o tempo decorrido atinge 2 segundos.
- Quando a tecla é solta, `current_key` e `press_time` são redefinidos para evitar disparos futuros desnecessários.
- O evento desejado pode ser disparado após 2 segundos de tecla pressionada.

Com isso, o evento será disparado apenas após a tecla ter sido pressionada por 2 segundos ou mais, antes de ser liberada.



---
```python
carga layers[2] preciona "u"

cargaLayoutEscolhido[2]
press "u" => keycode 117, keycodesToPosition[117] => 101
layout[1][0][1] = "1"
envia evendo "1" #if 103 == keycode: keyboard_controller.press('1') #1

```#python
---

programa transforma layouts/chars em position

positionToKeycode {}  
layoutCharToPosition {}
atualkeycodeToChar {}



se o keycode "oO" va ficar no position "103"

chama o dicc da posicaoKeycodes que retorna a position
posicaoKeycodes ("103") = 91 # 91 e, o keycode
actualLayout = entao 91 vai ser "oO"


---

si a key=62=m, no layer FNFSP

o programa vai ter que:

1. poder mudar o layer para FNFSP
    - escolhe layout na list
2. passa os atual keycodes na posição do layout
    - criar um dcc ex "k": "016"

---

3. transforma teclas em keycodes

- reconhecer 62 que é m
- procurar onde ficaria m no layer FNFSP
- enviar evento se for valido no layer FNFSP



 
# touch
## capturar o touch e transformar em um evento
## envio de eventos entre Esp32 e devices
## enviar Kb e Mouse Axis via Bluetooth
## trabalhar com eventos In/Out

# mudar o PT-Abnt2 eventos no linux
## fazer com que o pyton se ecxecute no inicio

# preTratamento do Kb
## remapeamento de teclas usando (arquivo Json)
### como pegar o mapping atual do teclado para saber os keycodes
### criar um jeito fácil de escrever os novos mapping e os layers
#### ## escrever os caracteres que eu quero usar e ele transforma eles em keycodes
## reconhecendo teclas simultânea - pressed_keys = set() pressed_keys.add(keycode) pressed_keys.discard(keycode)
## medir evento em unidade de tempo com time
## aceleração de tecla pressionada para o mouse

# tratamento do Kb
## usar os eventos e transformá-los em layers
## resolver como ativar e desativar layers

# construir sys modos VI para Kb


---



---

#
```python 
[
    [
        [01,02,03,04,05,06],
        [07,08,09,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
    ],
    [
        [01,02,03,04,05,06],
        [07,08,09,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
    ],
]


ESC = 001
qQ = 002
wW = 003
gG = 016
CR = 135


``` #



---
como se chama os caracteres em inglês:

'!','@','#','$','%','*','(',')','_','+','<','>',':','?','|','"','''
'+','{','}','`','^'

, = COMMA
. = PERIOD (OR FULL STOP IN BRITISH ENGLISH)
" = DOUBLE QUOTATION MARK (OR QUOTE)
' = SINGLE QUOTATION MARK (OR APOSTROPHE)
; = SEMICOLON
: = COLON
´ = ACUTE ACCENT (OR ACUTE)
` = GRAVE ACCENT (OR BACKTICK)
~ = TILDE
/ = FORWARD SLASH (OR SLASH)
( = LEFT PARENTHESIS (OR OPEN PARENTHESIS)
) = RIGHT PARENTHESIS (OR CLOSE PARENTHESIS)
\[ = BRACKETL (OR OPEN BRACKET, SQUARE BRACKET)
|] = BRACKETR (OR CLOSE BRACKET, SQUARE BRACKET)
{ = LEFT BRACE (OR OPENING BRACE, OR LEFT CURLY BRACKET)
} = RIGHT BRACE (OR CLOSING BRACE, OR RIGHT CURLY BRACKET)
\ = BACKSLASH
\_ = UNDERSCORE
- = HYPHEN (OR DASH)
= = EQUALS (OR EQUALS SIGN)
Ç = C CEDILLA (OR CEDILLA)
! = EXCLAMATION MARK
@ = AT SIGN (OR AT SYMBOL)
# = HASH (OR POUND SIGN IN THE U.S.)
$ = DOLLAR SIGN
% = PERCENT SIGN
* = ASTERISK
+ = PLUS SIGN
< = LESS THAN SIGN
> = GREATER THAN SIGN
? = QUESTION MARK
| = VERTICAL BAR (OR PIPE)
+ = PLUS SIGN
^ = CIRCUMFLEX  (OR CARET ACCENT)



---


xmodmap -e "keycode 64 = Super_L"
xmodmap -e "keycode 133 = Alt_L"
xmodmap -e "keycode 38 = Alt_L"

xmodmap -pke | grep -E "keycode (64|133)"

# desativa e ativar caps lock
```bash
setxkbmap -option caps:none
setxkbmap -option
```
# xev para ver os eventos
xev

# ver todos os keycodes atuais
xmodmap -pke

# instalar sxhkd
sudo pacman -S sxhkd

# criar arquivo layer1.sh

# rodar como executabla

chmod +x 00layer.sh
chmod +x layer1.sh
chmod +x layer2.sh


./layer1.sh
./00layer.sh


setxkbmap

---

back presure

---

setxkbmap -layout mouse -variant mousekeys
sudo chmod 644 /usr/share/X11/xkb/symbols/mouse

setxkbmap -print -verbose 10
setxkbmap -layout br -variant abnt2



# kbMapings kbMouseController

- usar mouse

- usar setas para mover

- rodar programa sem a consola aberta

- NoSymbol para layer0

- teclas em seu lugar com py remapear todo o teclado com python
    - onpress
    - release

- validar teclas sostenizas

- s-caps muda layers como ativar mouse

- win alt por alt win e win como opçao


# alt/win

xmodmap -e "keycode 64 = Super_L"
xmodmap -e "keycode 133 = Alt_L"


xmodmap -pke | grep -E "keycode (64|133)"


xmodmap ~/.Xmodmap

---

como python eu quero leer o xmodmap -pke e gerar um diccionario

xmodmap -pke

keycode   8 =
keycode   9 = Escape NoSymbol Escape
keycode  10 = 1 exclam 1 exclam onesuperior exclamdown onesuperior
keycode  11 = 2 at 2 at twosuperior onehalf twosuperior
keycode  12 = 3 numbersign 3 numbersign threesuperior threequarters threesuperior
keycode  13 = 4 dollar 4 dollar sterling onequarter sterling
keycode  14 = 5 percent 5 percent cent threeeighths cent
keycode  15 = 6 dead_diaeresis 6 dead_diaeresis notsign diaeresis notsign
keycode  16 = 7 ampersand 7 ampersand braceleft seveneighths braceleft
keycode  17 = 8 asterisk 8 asterisk bracketleft trademark bracketleft
keycode  18 = 9 parenleft 9 parenleft bracketright plusminus bracketright
keycode  19 = 0 parenright 0 parenright braceright degree braceright
keycode  20 = minus underscore minus underscore backslash questiondown backslash
keycode  21 = equal plus equal plus section dead_ogonek section
keycode  22 = BackSpace BackSpace BackSpace BackSpace NoSymbol NoSymbol Terminate_Server
keycode  23 = Tab ISO_Left_Tab Tab ISO_Left_Tab
keycode  24 = q Q q Q slash slash slash
keycode  25 = w W w W question question question
keycode  26 = e E e E degree degree degree
keycode  27 = r R r R registered registered registered
keycode  28 = t T t T tslash Tslash tslash
keycode  29 = y Y y Y leftarrow yen leftarrow
keycode  30 = u U u U downarrow uparrow downarrow
keycode  31 = i I i I rightarrow idotless rightarrow
keycode  32 = o O o O oslash Oslash oslash
keycode  33 = p P p P thorn THORN thorn
keycode  34 = dead_acute dead_grave dead_acute dead_grave acute grave acute
keycode  35 = bracketleft braceleft bracketleft braceleft ordfeminine dead_macron ordfeminine
keycode  36 = Return NoSymbol Return
keycode  37 = Control_L NoSymbol Control_L
keycode  38 = a A a A ae AE ae
keycode  39 = s S s S ssharp U1E9E ssharp
keycode  40 = d D d D eth ETH eth
keycode  41 = f F f F dstroke ordfeminine dstroke
keycode  42 = g G g G eng ENG eng
keycode  43 = h H h H hstroke Hstroke hstroke
keycode  44 = j J j J dead_hook dead_horn dead_hook
keycode  45 = k K k K kra ampersand kra
keycode  46 = l L l L lstroke Lstroke lstroke
keycode  47 = ccedilla Ccedilla ccedilla Ccedilla dead_acute dead_doubleacute dead_acute
keycode  48 = dead_tilde dead_circumflex dead_tilde dead_circumflex asciitilde asciicircum asciitilde
keycode  49 = apostrophe quotedbl apostrophe quotedbl notsign notsign notsign
keycode  50 = Shift_L NoSymbol Shift_L
keycode  51 = bracketright braceright bracketright braceright masculine masculine masculine
keycode  52 = z Z z Z guillemotleft less guillemotleft
keycode  53 = x X x X guillemotright greater guillemotright
keycode  54 = c C c C copyright copyright copyright
keycode  55 = v V v V doublelowquotemark singlelowquotemark doublelowquotemark
keycode  56 = b B b B leftdoublequotemark leftsinglequotemark leftdoublequotemark
keycode  57 = n N n N rightdoublequotemark rightsinglequotemark rightdoublequotemark
keycode  58 = m M m M mu mu mu
keycode  59 = comma less comma less U2022 multiply U2022
keycode  60 = period greater period greater periodcentered division periodcentered
keycode  61 = semicolon colon semicolon colon dead_belowdot dead_abovedot dead_belowdot
keycode  62 = Shift_R NoSymbol Shift_R
keycode  63 = KP_Multiply KP_Multiply KP_Multiply KP_Multiply KP_Multiply KP_Multiply XF86ClearGrab
keycode  64 = Alt_L Meta_L Alt_L Meta_L
keycode  65 = space NoSymbol space
keycode  66 = Caps_Lock NoSymbol Caps_Lock
keycode  67 = F1 F1 F1 F1 F1 F1 XF86Switch_VT_1
keycode  68 = F2 F2 F2 F2 F2 F2 XF86Switch_VT_2
keycode  69 = F3 F3 F3 F3 F3 F3 XF86Switch_VT_3
keycode  70 = F4 F4 F4 F4 F4 F4 XF86Switch_VT_4
keycode  71 = F5 F5 F5 F5 F5 F5 XF86Switch_VT_5
keycode  72 = F6 F6 F6 F6 F6 F6 XF86Switch_VT_6
keycode  73 = F7 F7 F7 F7 F7 F7 XF86Switch_VT_7
keycode  74 = F8 F8 F8 F8 F8 F8 XF86Switch_VT_8
keycode  75 = F9 F9 F9 F9 F9 F9 XF86Switch_VT_9
keycode  76 = F10 F10 F10 F10 F10 F10 XF86Switch_VT_10
keycode  77 = Num_Lock NoSymbol Num_Lock
keycode  78 = Scroll_Lock NoSymbol Scroll_Lock
keycode  79 = KP_Home KP_7 KP_Home KP_7
keycode  80 = KP_Up KP_8 KP_Up KP_8
keycode  81 = KP_Prior KP_9 KP_Prior KP_9
keycode  82 = KP_Subtract KP_Subtract KP_Subtract KP_Subtract KP_Subtract KP_Subtract XF86Prev_VMode
keycode  83 = KP_Left KP_4 KP_Left KP_4
keycode  84 = KP_Begin KP_5 KP_Begin KP_5
keycode  85 = KP_Right KP_6 KP_Right KP_6
keycode  86 = KP_Add KP_Add KP_Add KP_Add KP_Add KP_Add XF86Next_VMode
keycode  87 = KP_End KP_1 KP_End KP_1
keycode  88 = KP_Down KP_2 KP_Down KP_2
keycode  89 = KP_Next KP_3 KP_Next KP_3
keycode  90 = KP_Insert KP_0 KP_Insert KP_0
keycode  91 = KP_Delete KP_Separator KP_Delete KP_Separator
keycode  92 = ISO_Level3_Shift NoSymbol ISO_Level3_Shift
keycode  93 =
keycode  94 = backslash bar backslash bar dead_caron dead_breve dead_caron
keycode  95 = F11 F11 F11 F11 F11 F11 XF86Switch_VT_11
keycode  96 = F12 F12 F12 F12 F12 F12 XF86Switch_VT_12
keycode  97 = slash question slash question degree questiondown degree
keycode  98 = Katakana NoSymbol Katakana
keycode  99 = Hiragana NoSymbol Hiragana
keycode 100 = Henkan_Mode NoSymbol Henkan_Mode
keycode 101 = Hiragana_Katakana NoSymbol Hiragana_Katakana
keycode 102 = Muhenkan NoSymbol Muhenkan
keycode 103 =
keycode 104 = KP_Enter NoSymbol KP_Enter
keycode 105 = Control_R NoSymbol Control_R
keycode 106 = KP_Divide KP_Divide KP_Divide KP_Divide KP_Divide KP_Divide XF86Ungrab
keycode 107 = Print Sys_Req Print Sys_Req
keycode 108 = ISO_Level3_Shift NoSymbol ISO_Level3_Shift
keycode 109 = Linefeed NoSymbol Linefeed
keycode 110 = Home NoSymbol Home
keycode 111 = Up NoSymbol Up
keycode 112 = Prior NoSymbol Prior
keycode 113 = Left NoSymbol Left
keycode 114 = Right NoSymbol Right
keycode 115 = End NoSymbol End
keycode 116 = Down NoSymbol Down
keycode 117 = Next NoSymbol Next
keycode 118 = Insert NoSymbol Insert
keycode 119 = Delete NoSymbol Delete
keycode 120 =
keycode 121 = XF86AudioMute NoSymbol XF86AudioMute
keycode 122 = XF86AudioLowerVolume NoSymbol XF86AudioLowerVolume
keycode 123 = XF86AudioRaiseVolume NoSymbol XF86AudioRaiseVolume
keycode 124 = XF86PowerOff NoSymbol XF86PowerOff
keycode 125 = KP_Equal NoSymbol KP_Equal
keycode 126 = plusminus NoSymbol plusminus
keycode 127 = Pause Break Pause Break
keycode 128 = XF86LaunchA NoSymbol XF86LaunchA
keycode 129 = KP_Decimal KP_Decimal KP_Decimal KP_Decimal
keycode 130 = Hangul NoSymbol Hangul
keycode 131 = Hangul_Hanja NoSymbol Hangul_Hanja
keycode 132 =
keycode 133 = Super_L NoSymbol Super_L
keycode 134 = Super_R NoSymbol Super_R
keycode 135 = Menu NoSymbol Menu
keycode 136 = Cancel NoSymbol Cancel
keycode 137 = Redo NoSymbol Redo
keycode 138 = SunProps NoSymbol SunProps
keycode 139 = Undo NoSymbol Undo
keycode 140 = SunFront NoSymbol SunFront
keycode 141 = XF86Copy NoSymbol XF86Copy
keycode 142 = XF86Open NoSymbol XF86Open
keycode 143 = XF86Paste NoSymbol XF86Paste
keycode 144 = Find NoSymbol Find
keycode 145 = XF86Cut NoSymbol XF86Cut
keycode 146 = Help NoSymbol Help
keycode 147 = XF86MenuKB NoSymbol XF86MenuKB
keycode 148 = XF86Calculator NoSymbol XF86Calculator
keycode 149 =
keycode 150 = XF86Sleep NoSymbol XF86Sleep
keycode 151 = XF86WakeUp NoSymbol XF86WakeUp
keycode 152 = XF86Explorer NoSymbol XF86Explorer
keycode 153 = XF86Send NoSymbol XF86Send
keycode 154 =
keycode 155 = XF86Xfer NoSymbol XF86Xfer
keycode 156 = XF86Launch1 NoSymbol XF86Launch1
keycode 157 = XF86Launch2 NoSymbol XF86Launch2
keycode 158 = XF86WWW NoSymbol XF86WWW
keycode 159 = XF86DOS NoSymbol XF86DOS
keycode 160 = XF86ScreenSaver NoSymbol XF86ScreenSaver
keycode 161 = XF86RotateWindows NoSymbol XF86RotateWindows
keycode 162 = XF86TaskPane NoSymbol XF86TaskPane
keycode 163 = XF86Mail NoSymbol XF86Mail
keycode 164 = XF86Favorites NoSymbol XF86Favorites
keycode 165 = XF86MyComputer NoSymbol XF86MyComputer
keycode 166 = XF86Back NoSymbol XF86Back
keycode 167 = XF86Forward NoSymbol XF86Forward
keycode 168 =
keycode 169 = XF86Eject NoSymbol XF86Eject
keycode 170 = XF86Eject NoSymbol XF86Eject
keycode 171 = XF86AudioNext NoSymbol XF86AudioNext
keycode 172 = XF86AudioPlay XF86AudioPause XF86AudioPlay XF86AudioPause
keycode 173 = XF86AudioPrev NoSymbol XF86AudioPrev
keycode 174 = XF86AudioStop XF86Eject XF86AudioStop XF86Eject
keycode 175 = XF86AudioRecord NoSymbol XF86AudioRecord
keycode 176 = XF86AudioRewind NoSymbol XF86AudioRewind
keycode 177 = XF86Phone NoSymbol XF86Phone
keycode 178 =
keycode 179 = XF86Tools NoSymbol XF86Tools
keycode 180 = XF86HomePage NoSymbol XF86HomePage
keycode 181 = XF86Reload NoSymbol XF86Reload
keycode 182 = XF86Close NoSymbol XF86Close
keycode 183 =
keycode 184 =
keycode 185 = XF86ScrollUp NoSymbol XF86ScrollUp
keycode 186 = XF86ScrollDown NoSymbol XF86ScrollDown
keycode 187 = parenleft NoSymbol parenleft
keycode 188 = parenright NoSymbol parenright
keycode 189 = XF86New NoSymbol XF86New
keycode 190 = Redo NoSymbol Redo
keycode 191 = XF86Tools NoSymbol XF86Tools
keycode 192 = XF86Launch5 NoSymbol XF86Launch5
keycode 193 = XF86Launch6 NoSymbol XF86Launch6
keycode 194 = XF86Launch7 NoSymbol XF86Launch7
keycode 195 = XF86Launch8 NoSymbol XF86Launch8
keycode 196 = XF86Launch9 NoSymbol XF86Launch9
keycode 197 =
keycode 198 = XF86AudioMicMute NoSymbol XF86AudioMicMute
keycode 199 = XF86TouchpadToggle NoSymbol XF86TouchpadToggle
keycode 200 = XF86TouchpadOn NoSymbol XF86TouchpadOn
keycode 201 = XF86TouchpadOff NoSymbol XF86TouchpadOff
keycode 202 =
keycode 203 = ISO_Level5_Shift NoSymbol ISO_Level5_Shift
keycode 204 = NoSymbol Alt_L NoSymbol Alt_L
keycode 205 = NoSymbol Meta_L NoSymbol Meta_L
keycode 206 = NoSymbol Super_L NoSymbol Super_L
keycode 207 = NoSymbol Hyper_L NoSymbol Hyper_L
keycode 208 = XF86AudioPlay NoSymbol XF86AudioPlay
keycode 209 = XF86AudioPause NoSymbol XF86AudioPause
keycode 210 = XF86Launch3 NoSymbol XF86Launch3
keycode 211 = XF86Launch4 NoSymbol XF86Launch4
keycode 212 = XF86LaunchB NoSymbol XF86LaunchB
keycode 213 = XF86Suspend NoSymbol XF86Suspend
keycode 214 = XF86Close NoSymbol XF86Close
keycode 215 = XF86AudioPlay NoSymbol XF86AudioPlay
keycode 216 = XF86AudioForward NoSymbol XF86AudioForward
keycode 217 =
keycode 218 = Print NoSymbol Print
keycode 219 =
keycode 220 = XF86WebCam NoSymbol XF86WebCam
keycode 221 = XF86AudioPreset NoSymbol XF86AudioPreset
keycode 222 =
keycode 223 = XF86Mail NoSymbol XF86Mail
keycode 224 = XF86Messenger NoSymbol XF86Messenger
keycode 225 = XF86Search NoSymbol XF86Search
keycode 226 = XF86Go NoSymbol XF86Go
keycode 227 = XF86Finance NoSymbol XF86Finance
keycode 228 = XF86Game NoSymbol XF86Game
keycode 229 = XF86Shop NoSymbol XF86Shop
keycode 230 =
keycode 231 = Cancel NoSymbol Cancel
keycode 232 = XF86MonBrightnessDown NoSymbol XF86MonBrightnessDown
keycode 233 = XF86MonBrightnessUp NoSymbol XF86MonBrightnessUp
keycode 234 = XF86AudioMedia NoSymbol XF86AudioMedia
keycode 235 = XF86Display NoSymbol XF86Display
keycode 236 = XF86KbdLightOnOff NoSymbol XF86KbdLightOnOff
keycode 237 = XF86KbdBrightnessDown NoSymbol XF86KbdBrightnessDown
keycode 238 = XF86KbdBrightnessUp NoSymbol XF86KbdBrightnessUp
keycode 239 = XF86Send NoSymbol XF86Send
keycode 240 = XF86Reply NoSymbol XF86Reply
keycode 241 = XF86MailForward NoSymbol XF86MailForward
keycode 242 = XF86Save NoSymbol XF86Save
keycode 243 = XF86Documents NoSymbol XF86Documents
keycode 244 = XF86Battery NoSymbol XF86Battery
keycode 245 = XF86Bluetooth NoSymbol XF86Bluetooth
keycode 246 = XF86WLAN NoSymbol XF86WLAN
keycode 247 = XF86UWB NoSymbol XF86UWB
keycode 248 =
keycode 249 = XF86Next_VMode NoSymbol XF86Next_VMode
keycode 250 = XF86Prev_VMode NoSymbol XF86Prev_VMode
keycode 251 = XF86MonBrightnessCycle NoSymbol XF86MonBrightnessCycle
keycode 252 = XF86BrightnessAuto NoSymbol XF86BrightnessAuto
keycode 253 = XF86DisplayOff NoSymbol XF86DisplayOff
keycode 254 = XF86WWAN NoSymbol XF86WWAN
keycode 255 = XF86RFKill NoSymbol XF86RFKill


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


O `keyboard.Controller` é uma classe da biblioteca `pynput` que permite simular eventos de teclado, como pressionar e soltar teclas. Essa funcionalidade pode ser útil quando você deseja automatizar a entrada de teclado ou simular teclas em um programa.

Aqui está um exemplo básico de como usar o `keyboard.Controller` para simular o pressionamento e liberação de teclas:

### Exemplo básico de uso do `keyboard.Controller`:

```python
from pynput.keyboard import Key, Controller
import time

# Cria uma instância do Controller
keyboard_controller = Controller()

# Pressiona e solta uma tecla
keyboard_controller.press('a')
keyboard_controller.release('a')

# Simula a tecla shift + 'a' (que resulta em 'A')
keyboard_controller.press(Key.shift)
keyboard_controller.press('a')
keyboard_controller.release('a')
keyboard_controller.release(Key.shift)

# Escreve uma string inteira (como se estivesse digitando)
keyboard_controller.type('Hello, World!')

# Espera um pouco para ver a ação
time.sleep(1)
```

### Explicação dos principais métodos:
- `press(key)`: Pressiona a tecla especificada. Pode ser uma tecla regular (como `'a'`) ou uma tecla especial (como `Key.shift`).
- `release(key)`: Solta a tecla especificada.
- `type(string)`: Simula a digitação de uma string, uma tecla por vez.

### Exemplo mais avançado com teclas especiais:

Se você quiser usar teclas especiais como `Enter`, `Shift`, ou `Ctrl`, pode usar o módulo `pynput.keyboard.Key` para acessá-las:

```python
from pynput.keyboard import Key, Controller

# Cria uma instância do Controller
keyboard_controller = Controller()

# Pressiona e solta a tecla 'Enter'
keyboard_controller.press(Key.enter)
keyboard_controller.release(Key.enter)

# Simula Ctrl + 'c' (copiar)
keyboard_controller.press(Key.ctrl)
keyboard_controller.press('c')
keyboard_controller.release('c')
keyboard_controller.release(Key.ctrl)
```

Esses exemplos mostram como você pode simular eventos de teclado, como digitar caracteres, pressionar teclas especiais ou combinações de teclas.

---



```python
import json

def clearmd(lines):
    dcclayers = {}
    lines_cleans = []
    for line in lines:
        cleanitem = line.replace('\n', '').replace('\t', '').replace('*', '').replace(' ', '').strip()
        if cleanitem: # Apenas adiciona a line se não for vazia
            #lines_cleans.append(cleanitem)
            import ipdb; ipdb.set_trace()
            if cleanitem.startswith('#'):
                dcclayers[cleanitem.replace('#', '')] = {} 
            # if cleanitem.startswith('##'):
            #     print(cleanitem)


    return lines_cleans

def getmdlayers(layersfile, recjson):
    with open(layersfile, 'r') as filemd:
        lines = filemd.readlines()

    lines_cleans = clearmd(lines)

    with open(recjson, 'r') as arquivo:
        jsonKecodes = json.load(arquivo)

    reckeycodes = {valor[0]: chave for chave, valor in jsonKecodes.items()}

    return lines_cleans


{
    "FN0": {
        "FN0L": [
            { "ESC": 1, "qQ": 2 },
            { "TAB": 3, "aA": 4 },
        ],
        "FN0R": [
            { "yY": 5, "uU": 6 },
            { "hH": 7, "iJ": 8 },
        ],
    },
}



def parse_file_to_dict(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    layers = {}
    current_layer = None
    current_side = None
    key_counter = 1

    for line in lines:
        line = line.strip()

        if line.startswith('#'):
            current_layer = line[1:].strip()  # Nome da camada, como 'FN0'
            layers[current_layer] = {}

        elif line.startswith('##'):
            current_side = line[2:].strip()  # Nome do lado, como 'FN0L' ou 'FN0R'
            layers[current_layer][current_side] = []

        elif line:  # Processar as linhas de teclas
            keys = [key.strip("'") for key in line.split(',') if key.strip()]
            row_dict = {key: key_counter + i for i, key in enumerate(keys)}
            key_counter += len(keys)
            layers[current_layer][current_side].append(row_dict)

    return layers


# Exemplo de uso
filename = 'seu_arquivo.txt'
key_dict = parse_file_to_dict(filename)

# Imprimir o dicionário gerado
import pprint
pprint.pprint(key_dict)


``` # python



Eu quero um programa em python que transforme a entrada:

# FN0
## FN0L
'000',		'001',		'002',		'003',		'004',		'005'
'010',		'011',		'012',		'013',		'014',		'015'
'020',		'021',		'022',		'023',		'024',		'025'
'030',		'031',		'032',		'033',		'034',		'035'
## FN0R
'100',		'101',		'102',		'103',		'104',		'105'
'110',		'111',		'112',		'113',		'114',		'115'
'120',		'121',		'122',		'123',		'124',		'125'
'130',		'131',		'132',		'133',		'134',		'135'

# FN1
## FN1L
'ESC',		'qQ',		'wW',		'eE',		'rR',		'tT'
'TAB',		'aA',		'sS',		'dD',		'fF',		'gG'
'SL',		'ZZ',		'xX',		'cC',		'vV',		'bB'
'CL',		'FN4L',		'FN3L',		'FN2L',		'FN1L',		'SP'
## FNrR
'yY',		'uU',		'iI',		'oO',		'pP',		'B'
'hH',		'jJ',		'kK',		'lL',		'çÇ',		'E'
'nN',		'mM',		',<',		'.>',		';:',		'SR'
'SP',		'FN1R',		'FN2R',		'FN3R',		'FN4R',		'CR'


em essa lista:

```python
[
    [
        [
            ['000', '001', '002', '003', '004', '005'],
            ['010', '011', '012', '013', '014', '015'],
            ['020', '021', '022', '023', '024', '025'],
            ['030', '031', '032', '033', '034', '035']
        ],
        [
            ['100', '101', '102', '103', '104', '105'],
            ['110', '111', '112', '113', '114', '115'],
            ['120', '121', '122', '123', '124', '125'],
            ['130', '131', '132', '133', '134', '135']
        ]
    ],
    [
        [
            ['ESC', 'qQ', 'wW', 'eE', 'rR', 'tT'],
            ['TAB', 'aA', 'sS', 'dD', 'fF', 'gG'],
            ['SL', 'ZZ', 'xX', 'cC', 'vV', 'bB'],
            ['CL', 'FN4L', 'FN3L', 'FN2L', 'FN1L', 'SP']
        ],
        [
            ['yY', 'uU', 'iI', 'oO', 'pP', 'B'],
            ['hH', 'jJ', 'kK', 'lL', 'çÇ', 'E'],
            ['nN', 'mM', ',<', '.>', ';:', 'SR'],
            ['SP', 'FN1R', 'FN2R', 'FN3R', 'FN4R', 'CR']
        ]
    ]
]
```

lllsebastian     ççççk3k3k3j2k3j2k3j2k3j2k3l1k3j2uuiuooj2k3
