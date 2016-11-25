from grammar.complex.complexLY import parser as cmpx
from grammar.equation.equationLY import parser as eq

def cal(s):
    result = cmpx.parse(s)
    return result

def equation(s):
    result = eq.parse(s)
    val = result.split(';')
    print(val)
    eqn = val[0].replace('x', val[1])
    res = cal(eqn)
    return res