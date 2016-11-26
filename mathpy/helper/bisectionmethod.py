def bisectionmethod(eq, a, b, equation, maxIter=100, showIter=False):
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
        c = (a + b)/2
        aval = equation(eq + ';' + str(a))
        bval = equation(eq + ';' + str(b))
        cval = equation(eq + ';' + str(c))
        iterations.append([a, b, c, cval.real])
        if cval.real < 0:
            if bval.real < 0:
                b = c
            elif aval.real < 0:
                a = c
        elif cval.real > 0:
            if bval.real > 0:
                b = c
            elif aval.real > 0:
                a = c
        root = (a + b)/2
        if round(root, 4) == round(c, 4):
            if showIter == True:
                printIterations(iterations) 
            return root

def printIterations(iterations):
    print('Iterations\t  a\t  b\t  c\t  cval')
    for i in range(0, len(iterations)):
        print('    ' + str(i) + '\t\t'),
        for j in range(0, 4):
            print('{0:.4f}'.format(iterations[i][j]) + '\t'),
        print('')