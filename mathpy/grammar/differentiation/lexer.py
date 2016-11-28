import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'POW', 'LP', 'RP', 'MINUS', 'MUL'
)

t_LP = r'\('
t_RP = r'\)'
t_ID = r'(?![sin|cos|sec|cosec|tan|cot|log|ln|e|asin|acos|atan|sinh|cosh|tanh|asinh|acosh|atanh|j])[a-zA-Z][0-9a-zA-Z]*'
t_NUMBER = r'(|-)[0-9]*\.{0,1}[0-9]+'
t_POW = r'\^'
t_MUL = r'\*'
t_MINUS = r'-'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print('Illegal character', t)
    t.lexer.skip(1)

lexer = lex.lex()