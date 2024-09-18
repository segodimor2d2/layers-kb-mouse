def clearmd(lines):
    lines_cleans = []
    for line in lines:
        line_clean = line.replace('\n', '').replace('\t', '').replace('*', '').replace('#', '').strip()
        if line_clean: # Apenas adiciona a line se não for vazia
            lines_cleans.append(line_clean)
    return lines_cleans

def getmdlayers(filename):
    with open(filename, 'r') as filemd:
        lines = filemd.readlines()

    lines_cleans = clearmd(lines)

    return lines_cleans
