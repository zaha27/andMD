def main():
    print("%10s %10s %12s %10s %10s" % ('p', 'q', 'expr1', 'expr2', 'expr'))
    for p in (False, True):
        for q in (False, True):
            expr1 = p and (not q)
            expr2 = not p or q
            expr = not (expr1 and expr2)
            print("%10d %10d %10d %10d %10d" % (p, q, expr1, expr2, expr))

if __name__ == '__main__':
    main()

