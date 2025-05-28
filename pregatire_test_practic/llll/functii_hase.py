def citire_hasse(lista_noduri):
    d = {}
    for nod in lista_noduri:
        nr = int(input(f"nr adiacentii {nod}: "))
        vecini = []
        for i in range(nr):
            v = input(f"{' ':<3}Copilul {i+1} pentru {nod}: ")
            vecini.append(v)
        d[nod] = vecini
    return d

def citire_graf(n):
    graf = {}
    for i in range(n):
        x = input(f" nodul({i+1}): ")
        graf[x] = []
        print(f"pt {x}:")
        while True:
            vecin = input()
            if vecin == "":
                break
            graf[x].append(vecin)
    return graf