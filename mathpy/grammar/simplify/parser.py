import re
import ply.yacc as yacc
from mathpy.grammar.simplify.lexer import tokens

var = r'(?![sin|cos|sec|cosec|tan|cot|log|ln|e|asin|acos|atan|sinh|cosh|tanh|asinh|acosh|atanh|j])[a-zA-Z][0-9a-zA-Z]*'

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'POW')
)

def p_paran(t):
    'e : LP e RP'
    t[0] = t[1] + t[2] + t[3]

def p_expr(t):
    '''e : e POW e
         | e DIV e
         | e MUL e
         | e PLUS e
         | e MINUS e
    '''
    if t[2] == '^':
        if t[1] == '1':
            t[0] = t[1]
        elif t[1] == '0':
            t[0] = t[1]
        elif t[3] == '1':
            t[0] = t[1]
        elif t[3] == '0':
            t[0] = '1'
        else:
            try:
                n1 = float(t[1])
                n2 = float(t[3])
                t[0] = str(float(pow(n1, n2)))
            except ValueError:
                t[0] = t[1] + t[2] + t[3]
    elif t[2] == '/':
        if t[1] == '0':
            t[0] = t[1]
        elif t[3] == '1':
            t[0] = t[1]
        else:
            t[0] = t[1] + t[2] + t[3]
    elif t[2] == '*':
        if t[1] == '0' or t[3] == '0':
            t[0] = '0'
        elif t[1] == '1' and t[3] == '1':
            t[0] = '1'
        elif t[1] == '1':
            t[0] = t[3]
        elif t[3] == '1':
            t[0] = t[1]
        else:
            left = t[1].split('*')
            v1 = ''
            ind = -1
            n1 = 1
            n2 = 1
            ind2 = -1
            try:
                v2 = t[3][:t[3].index('^')]
            except ValueError:
                try:
                    n2 = float(t[3])
                    v2 = ''
                except ValueError:
                    v2 = t[3]
            if v2 != '':
                for i in range(0, len(left)):
                    r = re.search(v2, left[i])
                    if r:
                        v1 = '' + str(i)
                        ind = i
                        break
                    else:
                        try:
                            tv1 = left[i][:left[i].index('^')]
                        except ValueError:
                            tv1 = left[i]
                        if tv1 == v2:
                            v1 = tv1
                            ind = i
            else:
                for i in range(0, len(left)):
                    try:
                        n1 = float(left[i])
                        ind2 = i
                        break
                    except ValueError:
                        pass
            if v1 != '':
                v1 = left[ind]
                v2 = t[3]
            if len(v1) != 0 and len(v2) != 0:
                pw = 0.0
                try:
                    t1 = v1.index('^')
                except ValueError:
                    t1 = -1
                try:
                    t2 = v2.index('^')
                except ValueError:
                    t2 = -1
                if t1 > -1 and t2 > -1:
                    pw += float(v1[t1+1:]) + float(v2[t2+1:])
                elif t1 > -1:
                    pw += float(v1[t1+1:]) + 1
                elif t2 > -1:
                    pw += float(v2[t2+1:]) + 1
                if ind != -1:
                    if t1 > -1:
                        left[ind] = left[ind][:t1+1] + str(pw)
                    elif pw > 0.0:
                        left[ind] += '^' + str(pw)
                    else:
                        left[ind] += '^2'
                t[0] = '*'.join(left)
            elif n2 != 1:
                if ind2 != -1:
                    left[ind2] = str(float(left[ind2]) * n2)
                    t[0] = '*'.join(left)
                else:
                    t[0] = str(n2) + '*' + '*'.join(left)
            else:
                t[0] = t[1] + t[2] + t[3]
    elif t[2] == '+':
        if t[1] == '0' and t[3] == '0':
            t[0] = '0'
        elif t[1] == '0':
            t[0] = t[3]
        elif t[3] == '0':
            t[0] = t[1]
        else:
            left = t[1].split('+')
            t[0] = t[1] + t[2] + t[3]
    elif t[2] == '-':
        if t[1] == '0' and t[3] == '0':
            t[0] = '0'
        elif t[1] == '0':
            t[0] = t[3]
        elif t[3] == '0':
            t[0] = t[1]
        else:
            t[0] = t[1] + t[2] + t[3]

def p_id(t):
    'e : ID'
    t[0] = t[1]

def p_number(t):
    'e : NUMBER'
    t[0] = t[1]

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()