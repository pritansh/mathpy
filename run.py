import mathpy as mp

#real:2.0, imag:3.0
mp.cal('2+3i')

#real:6.0, imag:6.0
mp.cal('(2+3i)+(4+3i)')

#real:2.0, imag:9.0
mp.cal('((1+i)+(-1-i))+(2+9i)')

#real:0.0, imag:2.0
mp.cal('(1+i)^(2)')

#real:0.9, imag:1.09
mp.cal('(0.9+1.09i)')

#real:146.0
mp.equation('((x)^(2))+(2);12')