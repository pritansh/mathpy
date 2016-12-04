class Var:

    def __init__(self, var=[], coeff=[1], op=[]):
        self.var = var
        self.coeff = coeff
        self.op = op

    def __str__(self):
        return '(' + str(self.var) + ',' + str(self.coeff) + ',' + str(self.op) + ')'

    def __add__(self, obj):
        res = VarAdd(self, obj)
        return Var(res.var, res.coeff, res.op)

    def __radd__(self, obj):
        res = VarAdd(self, obj)
        return Var(res.var, res.coeff, res.op)

    def __mul__(self, obj):
        res = VarMul(self,obj)
        return Var(res.var, res.coeff, res.op)

    def __rmul__(self, obj):
        res = VarMul(self, obj)
        return Var(res.var, res.coeff, res.op)

    def disp(self):
        s = ''
        for i in range(0, len(self.var)):
            if self.coeff[i] != 1:
                    s += str(self.coeff[i]) + '*'
            if isinstance(self.var[i], list):
                s += '('
                for j in range(0, len(self.var[i])):
                    s += self.var[i][j]
                    if j != len(self.var[i])-1:
                        s += self.op[i][j]
                s += ')'
            elif len(s) == 0:
                s += self.var[i]
                if i != len(self.var)-1:
                    s += self.op[i]
            else:
                s += self.op[i] + self.var[i]
        return s


class VarAdd:

    def __init__(self, a=Var, b=Var):
        if isinstance(b, int):
            self.var = a.var + [str(b)]
            self.coeff = a.coeff + [1]
            self.op = a.op + ['+']

class VarMul:

    def __init__(self, a=Var, b=Var):
        if isinstance(b, int):
            self.var = [a.var]
            self.coeff = [e*b for e in a.coeff]
            self.op = a.op + [['*']]