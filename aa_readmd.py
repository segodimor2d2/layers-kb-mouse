import json
import pprint

def clearmd(lines):

    layers = {}
    current_layer = None
    current_side = None

    key_counter = 1
    dcclayers = {}
    lines_cleans = []

    for line in lines:
        line = line.replace('\n', '').replace('\t', '').replace(' ', '').strip()
        if line: # Apenas adiciona a line se não for vazia


            if line.startswith('#') and not line.startswith('##'):
                current_layer = line[1:].strip()  # Nome da camada, como 'FN0'
                layers[current_layer] = {}

            elif line.startswith('##'):
                current_side = line[2:].strip()  # Nome do lado, como 'FN0L' ou 'FN0R'
                layers[current_layer][current_side] = []

            else:
                keys = [key.strip("'") for key in line.split(',') if key.strip()]
                # row_dict = {key: key_counter + i for i, key in enumerate(keys)}
                # key_counter += len(keys)
                layers[current_layer][current_side].append(keys)

    pprint.pprint(layers)
    print(layers['FNFSP']['FNFSPL'][1])
    import ipdb; ipdb.set_trace()
    # print(layers['FNFSP']['FNFSPL'][2])
    # print(layers['FN0']['FN0L'])
    return layers

def getmdlayers(layersfile, recjson):

    with open(recjson, 'r') as arquivo:
        jsonKecodes = json.load(arquivo)

    reckeycodes = {valor[0]: chave for chave, valor in jsonKecodes.items()}

    with open(layersfile, 'r') as filemd:
        lines = filemd.readlines()

    lines_cleans = clearmd(lines)

    return lines_cleans

