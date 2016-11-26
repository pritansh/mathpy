import ply.yacc as yacc
from mathpy.grammar.equation.lexer import tokens

def p_b(t):
    'e : LP e RP'
    t[0] = t[1] + t[2] + t[3]

def p_id(t):
    'e : ID'
    t[0] = t[1]

def p_complex(t):
    'e : COMPLEX'
    t[0] = t[1]

def p_imag(t):
    'e : IMAG'
    t[0] = t[1]

def p_exp(t):
    '''e : LP e RP PLUS LP e RP
         | LP e RP MINUS LP e RP
         | LP e RP MUL LP e RP
         | LP e RP DIV LP e RP
         | LP e RP POW LP e RP
    '''
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7]

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