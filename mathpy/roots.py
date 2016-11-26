from mathpy.helper.durandkerner import durandkerner
from mathpy.helper.bisectionmethod import bisectionmethod
from mathpy.helper.regulafalsi import regulafalsi
from mathpy.grammar.paranthesis.parser import parser as paran
from mathpy.mt import cal, equation

def dk(s, maxIter=100, showIter=False):
    res = paran.parse(s)
    eq = res.split(';')
    root = []
    for i in range(0, int(eq[1])):
        root.append(cal('(0.4+0.9j)^' + str(i)))
    root = durandkerner(eq[0], root, equation, maxIter, showIter)
    if isinstance(root, str):
        return root
    else:
        root = [complex(round(e.real, 2), round(e.imag, 2)) for e in root]
        return root

def bm(s, a, b, maxIter=100, showIter=False):
    res = paran.parse(s)
    aval = equation(res + ';' + str(a))
    bval = equation(res + ';' + str(b))
    if aval.real > 0 and bval.real > 0:
        return 'Wrong values of a and b'
    elif aval.real < 0 and bval.real < 0:
        return 'Wrong values of a and b'
    else:
        root = bisectionmethod(res, a, b, equation, maxIter, showIter)
        if isinstance(root, str):
            return root
        else:
            root = round(root, 4)
            return root

def rf(s, a, b, maxIter=100, showIter=False):
    res = paran.parse(s)
    aval = equation(res + ';' + str(a))
    bval = equation(res + ';' + str(b))
    if aval.real > 0 and bval.real > 0:
        return 'Wrong values of a and b'
    elif aval.real < 0 and bval.real < 0:
        return 'Wrong values of a and b'
    else:
        root = regulafalsi(res, a, b, equation, maxIter, showIter)
        if isinstance(root, str):
            return root
        else:
            root = round(root, 4)
            return root