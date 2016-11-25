import re
from mathpy.helper.Complex import Complex
import ply.lex as lex

tokens = (
    'IMAG', 'NUMBER', 'COMPLEX', 'PLUS', 'MINUS', 'LP', 'RP',
    'MUL', 'DIV', 'POW'
    )

t_LP = r'\('
t_RP = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_POW = r'\^'
t_COMPLEX = r'(|-)[0-9]*\.{0,1}[0-9]+[+|-](|[0-9]*\.{0,1}[0-9]+)i'
t_IMAG = r'(|-)(|[0-9]*\.{0,1}[0-9]+)i'
t_NUMBER = r'(|-)[0-9]*\.{0,1}[0-9]+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print('Illegal character', t)
    t.lexer.skip(1)

lexer = lex.lex()

import ply.yacc as yacc

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'POW')
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
        try:
            if val.index('-', 1):
                indx = val.index('-', 1)
                v.append(val[:indx])
                v.append(val[indx+1:])
        except ValueError:
            pass
    v[1] = v[1].split('i')[0]
    if v[1] == '':
        v[1] = '1'
    t[0] = Complex(float(v[0]), float(v[1]))

def p_imag(t):
    'e : IMAG'
    val = t[1].split('i')[0]
    if val == '':
        val = '1'
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