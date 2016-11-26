import ply.lex as lex

tokens = (
    'IMAG', 'NUMBER', 'COMPLEX', 'PLUS', 'MINUS', 'LP', 'RP',
    'MUL', 'DIV', 'POW'
    )

t_LP = r'\('
t_RP = r'\)'
t_COMPLEX = r'(|-)[0-9]*\.{0,1}[0-9]+[\+|-](|[0-9]*\.{0,1}[0-9]+)j'
t_IMAG = r'(|-)(|[0-9]*\.{0,1}[0-9]+)j'
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