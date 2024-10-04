import json
import pprint

def getmdlayers(recjson):
    with open(recjson, 'r') as arquivo:
        charsToKeycodes = json.load(arquivo)

    keycodesToChars = {valor: chave for chave, valor in charsToKeycodes.items()}

    return charsToKeycodes, keycodesToChars

def process_layout(layersfile):
    with open(layersfile, 'r') as filemd:
        input_text = filemd.readlines()

    layers = []
    current_layer = []
    current_half = []

    for line in input_text:
        line = line.strip()

        if line.startswith('# FN'):
            if current_half:
                current_layer.append(current_half)
                current_half = []
            if current_layer:
                layers.append(current_layer)
                current_layer = []

        elif line.startswith('## FN'):
            if current_half:
                current_layer.append(current_half)
            current_half = []

        elif line:
            # Remove as aspas e transforma a linha em uma lista
            row = [item.strip().strip("'") for item in line.split(',') if item.strip()]
            current_half.append(row)

    # Adiciona o último half e layer
    if current_half:
        current_layer.append(current_half)
    if current_layer:
        layers.append(current_layer)

    return layers

def dccKeycodesToPositions(layers, charsToKeycodes):
    keycodesToPositions = {}
    positionsToKeycodes = {}

    for layer_idx, layer in enumerate(layers[0]):
        for row_idx, row in enumerate(layer):
            for col_idx, char in enumerate(row):
                keycode = charsToKeycodes[char]
                position = (layer_idx, row_idx, col_idx)
                keycodesToPositions[keycode] = position
                positionsToKeycodes[position] = keycode

    # pk = keycodesToPositions[117]
    # ver = layers[1][pk[0]][pk[1]][pk[2]]
    # import ipdb; ipdb.set_trace()
    # print(88888)

    return keycodesToPositions, positionsToKeycodes

def getTriggersPosition(layers):
    # Cria uma lista de listas vazias para cada camada
    posicoes = [[] for _ in range(len(layers))]

    for i, layer in enumerate(layers):
        for j, sublayer in enumerate(layer):
            for k, linha in enumerate(sublayer):
                for l, caractere in enumerate(linha):
                    if caractere == '@':
                        posicoes[i].append((j, k, l))  # Adiciona a posição relativa ao layer atual

    return posicoes

