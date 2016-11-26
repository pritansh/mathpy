import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'LP', 'RP', 'SC',
    'COMPLEX', 'IMAG', 'COMMA', 'SINE', 'COSINE', 'SECANT', 'COSECANT',
    'TANGENT', 'COTANGENT', 'LOG', 'LN', 'EXP'
)

t_LP = r'\('
t_RP = r'\)'
t_SC = r';'
t_COMMA = r','
t_SINE = r'sin'
t_COSINE = r'cos'
t_SECANT = r'sec'
t_COSECANT = r'cosec'
t_TANGENT = r'tan'
t_COTANGENT = r'cot'
t_LOG = r'log'
t_LN = r'ln'
t_EXP = r'e'
t_ID = r'(?![sin|cos|sec|cosec|tan|cot|log|ln|e|j])[a-zA-Z][0-9a-zA-Z]*'
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