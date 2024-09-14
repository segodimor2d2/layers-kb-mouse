import subprocess
import json
import re

def get_xmodmap_output():
    """Executa o comando xmodmap -pke e retorna a saída."""
    result = subprocess.run(['xmodmap', '-pke'], capture_output=True, text=True)
    return result.stdout

def parse_xmodmap_output(output):
    """Processa a saída do xmodmap e retorna um dicionário com keycodes e teclas."""
    keycode_map = {}
    
    # Regex para extrair keycode e suas teclas correspondentes
    pattern = re.compile(r"keycode\s+(\d+)\s*=\s*(\S+)\s*(\S*)")
    
    for line in output.splitlines():
        match = pattern.match(line)
        if match:
            keycode, *keys = match.groups()
            keycode = int(keycode)
            keycode_map[keycode] = keys
    
    return keycode_map

def save_to_json(data, filename):
    """Salva o dicionário de keycodes em um arquivo JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    xmodmap_output = get_xmodmap_output()
    keycode_map = parse_xmodmap_output(xmodmap_output)
    save_to_json(keycode_map, '66dkeycodes.json')
    print("Arquivo JSON gerado com sucesso.")

if __name__ == "__main__":
    main()
