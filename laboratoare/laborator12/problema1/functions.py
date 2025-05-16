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

def elementele_minimale(graf):
    lista = []
    toate = []
    for nod in graf:
        toate.append(nod)

    frecventa = []
    for nod in graf :
        lista_nod = graf[nod]
        for i in lista_nod :
            frecventa.append(i)
    lista = list(set(toate) - set(frecventa))
    return lista

def elementele_maximale(graf):
    lista = []
    for nod in graf :
        lista_nod = graf[nod]
        if lista_nod == [] :
            lista.append(nod)
    return lista

def elementul_maxim(graf):
    x = ''
    lista = elementele_maximale(graf)
    if len(lista) == 1 :
        return lista[0]
    else :
        return 'nu exista'

def elementul_minim(graf):
    x = ''
    lista = elementele_minimale(graf)
    if len(lista) == 1 :
        return lista[0]
    else :
        return 'nu exista'

def afisare_graf(graf) :
    for nod in graf :
        lista_nod = graf[nod]
        print(f"Nodul {nod} este acoperit de:", end = "")
        print(lista_nod)
    print()
