import mathpy as mp

#(-3+0j)
print(mp.cal('1+(-4)'))

#-4j
print(mp.cal('-4j'))

#(45-89j)
print(mp.cal('(2+4j)*(2-8j)+(9-81j)'))

#(-0.0959-0.936j)
print(mp.cal('(0.4+0.9j)^4'))

#(36+0j)
print(mp.equation('x*2+4;2^4'))

#(-9-4j)
print(mp.equation('x^2+y^2+(-8);(1+j)^2,2-j'))

#[(-1-0j), (-1+0j)]
print(mp.roots('x^2+2*x+1;2'))

#[(1+0j), (1-0j)]
print(mp.roots('x^2+(-2)*x+1;2'))

#[(0.38-0.92j), (0.38+0.92j), (-0.92+0.38j), (-0.92-0.38j), (-0.38-0.92j), (0.92-0.38j), (0.92+0.38j), (-0.38+0.92j)]
print(mp.roots('x^8+1;8'))