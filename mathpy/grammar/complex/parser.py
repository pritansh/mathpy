import ply.yacc as yacc
import cmath
from mathpy.grammar.complex.lexer import tokens

precedence = (
    ('nonassoc', 'SINE', 'COSINE', 'SECANT', 'COSECANT', 'TANGENT', 'COTANGENT', 'LOG', 'EXP', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'SINEH', 'COSINEH', 'TANGENTH', 'ARCSINEH', 'ARCCOSINEH', 'ARCTANGENTH'),
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
    v[1] = v[1].split('j')[0]
    if v[1] == '-' or v[1] == '':
        v[1]+= '1' 
    t[0] = complex(float(v[0]), float(v[1]))

def p_imag(t):
    'e : IMAG'
    val = t[1].split('j')[0]
    if val == '-' or val == '':
        val+= '1'
    t[0] = complex(0, float(val))

def p_expr(t):
    '''e : LP e RP POW LP e RP
         | LP e RP DIV LP e RP
         | LP e RP MUL LP e RP
         | LP e RP PLUS LP e RP
         | LP e RP MINUS LP e RP
    '''
    if t[4] == '^':
        t[0] = pow(t[2], t[6])
    elif t[4] == '/':
        t[0] = t[2] / t[6]
    elif t[4] == '*':
        t[0] = t[2] * t[6]
    elif t[4] == '+':
        t[0] = t[2] + t[6]
    elif t[4] == '-':
        t[0] = t[2] - t[6]

def p_sine(t):
    '''e : SINE LP e RP
         | COSINE LP e RP
         | SECANT LP e RP
         | COSECANT LP e RP
         | TANGENT LP e RP
         | COTANGENT LP e RP
         | LOG LP e COMMA e RP
         | LN LP e RP
         | EXP POW LP e RP
         | ARCSINE LP e RP
         | ARCCOSINE LP e RP
         | ARCTANGENT LP e RP
         | SINEH LP e RP
         | COSINEH LP e RP
         | TANGENTH LP e RP
         | ARCSINEH LP e RP
         | ARCCOSINEH LP e RP
         | ARCTANGENTH LP e RP
    '''
    if t[1] == 'sin':
        t[0] = cmath.sin(t[3])
    elif t[1] == 'cos':
        t[0] = cmath.cos(t[3])
    elif t[1] == 'sec':
        t[0] = 1/cmath.cos(t[3])
    elif t[1] == 'cosec':
        t[0] = 1/cmath.sin(t[3])
    elif t[1] == 'tan':
        t[0] = cmath.tan(t[3])
    elif t[1] == 'cot':
        t[0] = 1/cmath.tan(t[3])
    elif t[1] == 'log':
        t[0] = cmath.log(t[3], t[5])
    elif t[1] == 'ln':
        t[0] = cmath.log(t[3], cmath.e)
    elif t[1] == 'e':
        t[0] = cmath.exp(t[4])
    elif t[1] == 'asin':
        t[0] = cmath.asin(t[3])
    elif t[1] == 'acos':
        t[0] = cmath.acos(t[3])
    elif t[1] == 'atan':
        t[0] = cmath.atan(t[3])
    elif t[1] == 'sinh':
        t[0] = cmath.sinh(t[3])
    elif t[1] == 'cosh':
        t[0] = cmath.cosh(t[3])
    elif t[1] == 'tanh':
        t[0] = cmath.tanh(t[3])
    elif t[1] == 'asinh':
        t[0] = cmath.asinh(t[3])
    elif t[1] == 'acosh':
        t[0] = cmath.acosh(t[3])
    elif t[1] == 'atanh':
        t[0] = cmath.atanh(t[3])

def p_number(t):
    'e : NUMBER'
    t[0] = complex(float(t[1]), 0)

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()