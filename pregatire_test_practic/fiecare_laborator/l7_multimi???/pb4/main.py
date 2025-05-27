U = {1,2,3,4,5,6,7,8,9,10}
A = {2,4,6,8,10}

def multime_to_bits(A, U) :
    lista = []
    for x in U:
        if x in A:
            lista.append('1')
        else:
            lista.append('0')

    configuratie = ''.join(lista)

    return configuratie

def main() :
    configuratie_A = multime_to_bits(A,U)
    print(configuratie_A)
    print('complementul lui A')
    return

if __name__ == "__main__" :
    main()