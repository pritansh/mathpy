import ply.yacc as yacc
from mathpy.grammar.paranthesis.lexer import tokens

precedence = (
    ('nonassoc', 'NUMBER'),
    ('nonassoc', 'SINE', 'COSINE', 'SECANT', 'COSECANT', 'TANGENT', 'COTANGENT', 'LOG', 'EXP', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'SINEH', 'COSINEH', 'TANGENTH', 'ARCSINEH', 'ARCCOSINEH', 'ARCTANGENTH'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'POW'),
    ('nonassoc', 'COMPLEX')
    )

def p_b(t):
    'e : LP e RP'
    t[0] = t[2]

def p_id(t):
    'e : ID'
    t[0] = t[1]

def p_complex(t):
    'e : COMPLEX'
    t[0] = '(' + t[1] + ')'

def p_imag(t):
    'e : IMAG'
    t[0] = '(' + t[1] + ')'

def p_exp(t):
    '''e : e POW e
         | e PLUS e
         | e MINUS e
         | e MUL e
         | e DIV e
    '''
    t[0] = '(' + t[1] + ')' + t[2] + '(' + t[3] + ')'

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
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'cos':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'sec':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'cosec':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'tan':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'cot':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'log':
        t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6]
    elif t[1] == 'ln':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'e':
        t[0] = t[1] + t[2] + t[3] + t[4] + t[5]
    elif t[1] == 'asin':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'acos':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'atan':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'sinh':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'cosh':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'tanh':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'asinh':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'acosh':
        t[0] = t[1] + t[2] + t[3] + t[4]
    elif t[1] == 'atanh':
        t[0] = t[1] + t[2] + t[3] + t[4]

def p_val(t):
    '''e : e SC g
       g : g COMMA e
         | e
    '''
    if len(t) == 4:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1]

def p_number(t):
    'e : NUMBER'
    t[0] = t[1]

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()