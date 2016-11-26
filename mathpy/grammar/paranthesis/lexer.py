import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'LP', 'RP', 'SC',
    'COMPLEX', 'IMAG', 'COMMA'
)

t_LP = r'\('
t_RP = r'\)'
t_SC = r';'
t_COMMA = r','
t_ID = r'[a-hj-zA-HJ-Z][0-9a-hj-zA-HJ-Z]*'
t_COMPLEX = r'(|-)[0-9]*\.{0,1}[0-9]+[\+|-](|[0-9]*\.{0,1}[0-9]+)i'
t_IMAG = r'(|-)(|[0-9]*\.{0,1}[0-9]+)i'
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