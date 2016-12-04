def regulafalsi(eq, a, b, equation, maxIter=100, showIter=False):
    a = float(a)
    b = float(b)
    root = 0.0
    iterations = []
    iters = 0
    while True:
        iters += 1
        if iters == maxIter:
            if showIter == True:
                printIterations(iterations)
            return 'Not able to find a root'
        aval = equation(eq + ';' + str(a))
        bval = equation(eq + ';' + str(b))
        c = ((a*bval)-(b*aval))/(bval-aval)
        c = c.real
        cval = equation(eq + ';' + str(c))
        r = aval * cval
        iterations.append([a, b, c, r.real])
        if r.real < 0:
            b = c
        else:
            a = c
        aval = equation(eq + ';' + str(a))
        bval = equation(eq + ';' + str(b))
        root = ((a*bval)-(b*aval))/(bval-aval)
        root = root.real
        if round(root, 4) == round(c, 4):
            if showIter == True:
                printIterations(iterations) 
            return root

def printIterations(iterations):
    print('Iterations\t  a\t  b\t  c\t  f(a)*f(c)')
    for i in range(0, len(iterations)):
        print('    ' + str(i) + '\t\t'),
        for j in range(0, 4):
            print('{0:.4f}'.format(iterations[i][j]) + '\t'),
            if j == 2:
                print('  '),
        print('')