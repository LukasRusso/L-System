import json

def LSystem(numIteracoes, axiom, rules):
    print("Construindo ...")
    inicioString = axiom
    finalString = ""
    for i in range(numIteracoes):
        finalString = procString(inicioString, rules)
        inicioString = finalString

    return finalString

def procString(oldStr, rules):
    novaString = ""
    for ch in oldStr:
        novaString = novaString + AplicaRegra(ch, rules)

    return novaString

def AplicaRegra(caracter, rules):
    novaString = ""

    if caracter in rules:
        novaString = rules[caracter]
    else:
        novaString = caracter    

    return novaString

def desenhaLsystem(desenhar, stringInstr, angulo, comprimento, initX, initY):
    svg = '<svg height="15000" width="15000">'
    coordX = initX
    coordY = initY
    dirVetorial = 'R' # Right (R) / Left (L) / Up (U) / Down (D)

    for cmd in stringInstr:
        if cmd == 'F':            
            svg = svg + "\n" + createLineSVG(coordX, coordY, dirVetorial, comprimento)
            coordX = updateCoord(coordX, dirVetorial, True, comprimento)
            coordY = updateCoord(coordY, dirVetorial, False, comprimento) 
        elif cmd == '+':                     
            dirVetorial = anguloVetorial(dirVetorial, 'R')
        elif cmd == "-":            
            dirVetorial = anguloVetorial(dirVetorial, 'L')

    svg = svg + '</svg>'
    return svg

def updateCoord(coord, char, x, comp):
    if x:
        if char == 'R':
            return (coord + comp)        
        elif char == 'L':
            return (coord - comp)    
        else:
            return coord    
    else:
        if char == 'U':
            return (coord - comp)     
        elif char == 'D':
            return (coord + comp)
        else:
            return coord

def anguloVetorial(char, sentido):
    if sentido == 'R':
        if char == 'R':
            return 'D'
        elif char == 'D':
            return 'L'
        elif char == 'L':
            return 'U'
        elif char == 'U':
            return 'R'
    else:
        if char == 'R':
            return 'U'
        elif char == 'U':
            return 'L'
        elif char == 'L':
            return 'D'
        elif char == 'D':
            return 'R'

def createLineSVG(x: int, y: int, dir, compr: int):
    if dir == 'R':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, (x + compr), y)
    elif dir == 'L':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, (x - compr), y)
    elif dir == 'U':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, x, (y - compr))
    elif dir == 'D':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, x, (y + compr))

def lerArquivo():  
    json_file = open('gramatica.txt', 'tr', encoding="utf8")        
    data = json.load(json_file)        
    return data

def main():
    object = lerArquivo()
    axiom = object["axiom"]
    rules = object["rules"]
    initX = int(object["initX"])
    initY = int(object["initY"])    

    finalString = LSystem(15, axiom, rules) # cria a string para desenho
    svgArq = desenhaLsystem(True, finalString, 90, 5, initX, initY)     

    arquivo = open("L-System.html","w", encoding="utf-8")
    arquivo.write(svgArq)
    arquivo.close()

    print('Arquivo Constriuido')

main()