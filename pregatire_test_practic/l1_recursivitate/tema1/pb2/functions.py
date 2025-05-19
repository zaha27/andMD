def ridicare_la_putere(n, k) :
    if k == 0 :
        return 1
    else :
        return n * ridicare_la_putere(n, k - 1)