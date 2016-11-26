import re
from mathpy.grammar.complex.parser import parser as cmpx
from mathpy.grammar.equation.parser import parser as eq

def cal(s):
    result = cmpx.parse(s)
    return result

def equation(s):
    result = eq.parse(s)
    parts = result.split(';')
    chars = re.findall(r'[a-zA-Z][0-9a-zA-Z]*', parts[0])
    unique = sorted(set(chars), key=chars.index)
    vals = parts[1].split(',')
    for i in range(0, len(unique)):
        vals[i] = str(cmpx.parse(vals[i]))
        parts[0] = parts[0].replace(unique[i], vals[i])
    res = cmpx.parse(parts[0])
    return res