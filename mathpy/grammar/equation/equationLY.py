import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'LP', 'RP', 'SC'
)

t_LP = r'\('
t_RP = r'\)'
t_SC = r';'
t_ID = r'[a-zA-Z][0-9a-zA-Z]*'
t_NUMBER = r'(|-)[0-9]*\.{0,1}[0-9]+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_POW = r'\^'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print('Illegal character', t)
    t.lexer.skip(1)

lexer = lex.lex()

import ply.yacc as yacc

def p_b(t):
    'e : LP e RP'
    t[0] = t[1] + t[2] + t[3]

def p_id(t):
    'e : ID'
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
    'e : e SC NUMBER'
    t[0] = t[1] + t[2] + t[3]

def p_number(t):
    'e : NUMBER'
    t[0] = t[1]

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()