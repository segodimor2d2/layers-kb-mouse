import json

jsonfile_keycodes = '10recKeycodes.json'
with open(jsonfile_keycodes, 'r') as arquivo:
    jsonKecodes = json.load(arquivo)

dicc_keycodes = {valor[0]: chave for chave, valor in jsonKecodes.items()}

import ipdb; ipdb.set_trace()

