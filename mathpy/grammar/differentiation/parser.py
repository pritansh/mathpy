import ply.yacc as yacc
from mathpy.grammar.differentiation.lexer import tokens

def p_expr(t):
    '''e : LP e RP DIV LP e RP
       e : LP e RP MUL LP e RP
       e : LP e RP PLUS LP e RP
       e : LP e RP MINUS LP e RP
    '''
    t[0] = [t[2]] + [t[4]] + [t[6]]

def p_id(t):
    'e : ID'
    t[0] = t[1]

def p_number(t):
    'e : NUMBER'
    t[0] = t[1]

def p_error(t):
    print('Syntax error', t)

parser = yacc.yacc()