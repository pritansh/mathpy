import ply.yacc as yacc
from mathpy.helper.Complex import Complex
from mathpy.grammar.complex.lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'POW'),
    ('nonassoc', 'COMPLEX')
    )

def p_b(t):
    'e : LP e RP'
    t[0] = t[2]

def p_complex(t):
    'e : COMPLEX'
    val = t[1]
    v = []
    try:
        if val.index('+', 1):
            v = val.split('+')
    except ValueError:
        if val.index('-', 1):
            indx = val.index('-', 1)
            v.append(val[:indx])
            v.append(val[indx:])
    v[1] = v[1].split('i')[0]
    if v[1] == '-' or v[1] == '':
        v[1]+= '1' 
    t[0] = Complex(float(v[0]), float(v[1]))

def p_imag(t):
    'e : IMAG'
    val = t[1].split('i')[0]
    if val == '-' or val == '':
        val+= '1'
    t[0] = Complex(0, float(val))

def p_expr(t):
    '''e : LP e RP POW LP NUMBER RP
         | LP e RP DIV LP e RP
         | LP e RP MUL LP e RP
         | LP e RP PLUS LP e RP
         | LP e RP MINUS LP e RP
    '''
    if t[4] == '^':
        t[0] = t[2].pow(float(t[6]))
    elif t[4] == '/':
        t[0] = t[2].div(t[6])
    elif t[4] == '*':
        t[0] = t[2].mul(t[6])
    elif t[4] == '+':
        t[0] = t[2].add(t[6])
    elif t[4] == '-':
        t[0] = t[2].sub(t[6])

def p_number(t):
    'e : NUMBER'
    t[0] = Complex(float(t[1]), 0)

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()