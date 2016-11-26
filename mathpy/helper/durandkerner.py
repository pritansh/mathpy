import functools as ft

def durandkerner(eq, root, equation, maxIter=100, showIter=False):
    roots = []
    iterations = []
    iters = 0
    while True:
        iters += 1
        iterations.append([complex(round(e.real, 4), round(e.imag, 4)) for e in root])
        if iters == maxIter:
            if showIter == True:
                printIterations(iterations, root)
            return 'Not able to find roots'
        if len(roots) == len(root):
            t1 = [complex(round(e.real, 4), round(e.imag, 4)) for e in root]
            t2 = [complex(round(e.real, 4), round(e.imag, 4)) for e in roots]
            if t1 == t2:
                if show == True:
                    printIterations(iterations, root)                   
                return t2
            root = t2
            roots = []
        num = []
        denom = []
        for i in range(0, len(root)):
            num.append(equation(eq + ';' + str(root[i])))
            curr = root[i]
            temp = []
            for j in range(0, len(root)):
                if i != j:
                   temp.append(curr - root[j])
            denom.append(ft.reduce(lambda x,y:x*y, temp))
            if num[i] == complex(0, 0):
                roots.append(root[i])
            else:
                roots.append(root[i] - (num[i]/denom[i]))

def printIterations(iterations, root):
    p1 = '{0.real:.4f}'
    p2 = '{0.imag:.4f}j'
    p = ''
    print('Iterations\t     '),
    for i in range(0, len(root)):
        print('root' + str(i) + '\t\t    '),
    print('')
    for i in range(0, len(iterations)):
        print('   ' + str(i) + '\t\t'),
        for j in range(0, len(root)):
            if iterations[i][j].imag < 0:
                p = p1 + p2
            else:
                p = p1 + '+' + p2
            print(p.format(iterations[i][j]) + '\t\t'),
        print('')