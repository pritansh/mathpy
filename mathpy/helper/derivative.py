from mathpy.grammar.simplify.lexer import lexer as smpllex
from mathpy.grammar.simplify.parser import parser as smpl

class Derivative:
    
    def __init__(self, fn, dfn=''):
        self.fxn = fn
        self.dfxn = dfn

    def __str__(self):
        return '(' + self.fxn + ',' + self.dfxn + ')'

    def __add__(self, obj):
        self.diff()
        obj.diff()
        fxn = self.fxn + '+' + obj.fxn
        dfxn = '(' + self.dfxn + '+' + obj.dfxn + ')'
        dfxn = smpl.parse(dfxn, lexer=smpllex)
        return Derivative(fxn, dfn=dfxn)

    def __sub__(self, obj):
        self.diff()
        obj.diff()
        fxn = self.fxn + '-' + obj.fxn
        dfxn = '(' + self.dfxn + '-' + obj.dfxn + ')'
        dfxn = smpl.parse(dfxn, lexer=smpllex)
        return Derivative(fxn, dfn=dfxn)

    def __mul__(self, obj):
        self.diff()
        obj.diff()
        fxn = self.fxn + '*' + obj.fxn
        dfxn = '(' + self.dfxn + '*' + obj.fxn + '+' + self.fxn + '*' + obj.dfxn + ')'
        dfxn = smpl.parse(dfxn,lexer=smpllex)
        return Derivative(fxn, dfn=dfxn)

    def __truediv__(self, obj):
        self.diff()
        obj.diff()
        fxn = self.fxn + '/' + obj.fxn
        dfxn = '(' + self.dfxn + '*' + obj.fxn + '-' + self.fxn + '*' + obj.dfxn + ')/(' + obj.fxn + '^2)'
        dfxn = smpl.parse(dfxn,lexer=smpllex)
        return Derivative(fxn, dfn=dfxn)

    def diff(self):
        if self.dfxn == '':
            if self.fxn == 'x':
                self.dfxn = '1'
            else:
                self.dfxn = '0'

class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def AST(text):
    root = None
    if len(text) == 3:
        left = AST(text[0])
        if left == None:
            left = Node(text[0])
        right = Node(text[2])
        root = Node(text[1], left, right)
    return root

def differentiate(tree):
    if(tree.left or tree.right):
        left = differentiate(tree.left)
        right = differentiate(tree.right)
        u = None
        v = None
        if isinstance(left, Derivative):
            u = Derivative(left.fxn, dfn=left.dfxn)
        else:
            u = Derivative(left)
        if isinstance(right, Derivative):
            v = Derivative(right.fxn, dfn=right.dfxn)
        else:
            v = Derivative(right)
        if tree.data == '/':
            return u / v
        elif tree.data == '*':
            return u * v
        elif tree.data == '+':
            return u + v
        elif tree.data == '-':
            return u - v
    else:
        return tree.data