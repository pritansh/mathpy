from mathpy.helper.durandkerner import durandkerner
from mathpy.helper.bisectionmethod import bisectionmethod
from mathpy.helper.regulafalsi import regulafalsi
from mathpy.grammar.paranthesis.lexer import lexer as paranlex
from mathpy.grammar.paranthesis.parser import parser as paran
from mathpy.mt import cal, equation, plot

def dk(s, maxIter=100, showIter=False, plotGraph=False):
    res = paran.parse(s, lexer=paranlex)
    eq = res.split(';')
    root = []
    for i in range(0, int(eq[1])):
        root.append(cal('(0.4+0.9j)^' + str(i)))
    root = durandkerner(eq[0], root, equation, maxIter, showIter)
    if isinstance(root, str):
        return root
    else:
        root = [complex(round(e.real, 2), round(e.imag, 2)) for e in root]
        vals = []
        if plotGraph == True:
            x = [e.real for e in root]
            y = [e.imag for e in root]
            vals = [x, y]
            plot(eq[0], name=s.split(';')[0], val=vals, valname='Roots (Durand Kerner Method)')
        return root

def bm(s, a, b, maxIter=100, showIter=False, plotGraph=False):
    res = paran.parse(s, lexer=paranlex)
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
            vals = []
            if plotGraph == True:
                vals = [[root], [0]]
                plot(res, name=s, val=vals, valname='Root (Bisection Method)')
            return root

def rf(s, a, b, maxIter=100, showIter=False, plotGraph=False):
    res = paran.parse(s, lexer=paranlex)
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
            vals = []
            if plotGraph == True:
                vals = [[root], [0]]
                plot(res, name=s, val=vals, valname='Roots (Regula Falsi Method)')
            return root