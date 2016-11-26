import re
from mathpy.grammar.complex.parser import parser as cmpx
from mathpy.grammar.paranthesis.parser import parser as paran
from mathpy.helper.durandkerner import durandkerner

def cal(s):
    s = paran.parse(s)
    result = cmpx.parse(s)
    return result

def equation(s):
    result = paran.parse(s)
    try:
        if result.index(';'):
            parts = result.split(';')
            chars = re.findall(r'[a-ik-zA-IK-Z][0-9a-ik-zA-IK-Z]*', parts[0])
            unique = sorted(set(chars), key=chars.index)
            vals = parts[1].split(',')
            for i in range(0, len(unique)):
                vals[i] = str(cmpx.parse(vals[i]))
                vals[i] = vals[i].replace('(', '')
                vals[i] = vals[i].replace(')', '')
                parts[0] = parts[0].replace(unique[i], vals[i])
            res = cmpx.parse(parts[0])
            return res
    except ValueError:
        pass
    return result

def dk(s, showIter=False):
    res = paran.parse(s)
    eq = res.split(';')
    root = []
    for i in range(0, int(eq[1])):
        root.append(cal('(0.4+0.9j)^' + str(i)))
    root = durandkerner(eq[0], root, equation, showIter)
    root = [complex(round(e.real, 2), round(e.imag, 2)) for e in root]
    return root