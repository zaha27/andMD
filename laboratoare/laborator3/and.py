def main():
    print("%10s %10s %11s" % ('p', 'q', 'p and q'))
    for p in (False, True):
        for q in (False, True):
            print ("%10s %10s %10s" % ( p, q, p and q))
if __name__ == '__main__':
    main()
