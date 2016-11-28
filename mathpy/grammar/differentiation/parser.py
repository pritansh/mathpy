import ply.yacc as yacc
from mathpy.grammar.differentiation.lexer import tokens

precedence = (
    ('left', 'MUL'),
    ('right', 'POW')
)

def p_expr(t):
    'e : LP ID RP POW LP NUMBER RP'
    if float(t[6]) - 1.00 == 0:
        t[0] = '1'
    else:
        tt = str(float(t[6]) - 1.00)
        t[0] = t[6] + '*' + t[2] + t[4] + tt

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()