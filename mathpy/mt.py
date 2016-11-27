import re
from mathpy.grammar.complex.parser import parser as cmpx
from mathpy.grammar.paranthesis.parser import parser as paran

def cal(s):
    s = paran.parse(s)
    result = cmpx.parse(s)
    return result

def equation(s):
    result = paran.parse(s)
    try:
        if result.index(';'):
            parts = result.split(';')
            chars = re.findall(r'(?![sin|cos|sec|cosec|tan|cot|log|ln|e|asin|acos|atan|sinh|cosh|tanh|asinh|acosh|atanh|j])[a-zA-Z][0-9a-zA-Z]*', parts[0])
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