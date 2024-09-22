import json
import pprint

def process_layout(input_text):
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

    pprint.pprint(layers)
    import ipdb; ipdb.set_trace()
    return layers

def getmdlayers(layersfile, recjson):

    with open(recjson, 'r') as arquivo:
        jsonKecodes = json.load(arquivo)

    reckeycodes = {valor[0]: chave for chave, valor in jsonKecodes.items()}

    with open(layersfile, 'r') as filemd:
        lines = filemd.readlines()

    layers = process_layout(lines)

    return lines_cleans

