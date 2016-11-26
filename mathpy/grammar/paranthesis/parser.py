import ply.yacc as yacc
from mathpy.grammar.paranthesis.lexer import tokens

precedence = (
    ('nonassoc', 'NUMBER'),
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