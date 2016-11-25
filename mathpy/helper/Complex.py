import math

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag != 0:
            return 'real: ' + str(round(self.real, 2)) + ', imag: ' + str(round(self.imag, 2))
        else:
            return str(self.real)

    def conj(self):
        return Complex(self.real, -self.imag)

    def add(self, cpx):
        real = self.real + cpx.real
        if cpx.imag != 0:
            imag = self.imag + cpx.imag
        else:
            imag = self.imag
        return Complex(real, imag)

    def sub(self, cpx):
        real = self.real - cpx.real
        if cpx.imag != 0:
            imag = self.imag - cpx.imag
        else:
            imag = self.imag
        return Complex(real, imag)

    def mul(self, cpx):
        real = self.real * cpx.real - self.imag * cpx.imag
        imag = self.real * cpx.imag + self.imag * cpx.real
        return Complex(real, imag)

    def div(self, cpx):
        denom = cpx.real * cpx.real + cpx.imag * cpx.imag
        m = self.mul(cpx.conj())
        return Complex(m.real, m.imag)

    def pow(self, exp):
        mod = math.sqrt(self.real * self.real + self.imag * self.imag)
        angle = math.atan2(self.imag, self.real)
        t1 = exp * math.log(mod)
        t2 = exp * angle
        m = math.exp(t1)
        return Complex(m * math.cos(t2), m * math.sin(t2))
