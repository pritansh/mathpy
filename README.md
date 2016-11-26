# Mathpy

## Prerequisites
### Python 2 or Python 3
### Install ply using
    pip install ply

## If any error occurs, check order of paranthesis
## Negative numbers should be enclosed in paranthesis
### Example
  Evaluates -> 1 - 4

    import mathpy as mp
    print(mp.cal('1+(-4)'))
    
    (-3+0j)

## Features
### Complex Number Calculation
#### Basic
  Evaluates -> (-4j)

    import mathpy as mp
    print(mp.cal('-4j'))
  
    -4j

#### Multiple
  Evaluates -> (2+4j)*(2-8j)+(9-81j)

    import mathpy as mp
    print(mp.cal('(2+4j)*(2-8j)+(9-81j)'))

    (45-89j)

#### Power
  Evaluates -> (0.4+0.9j)<sup>4</sup>

    import mathpy as mp
    print(mp.cal('(0.4+0.9j)^4'))
  
    (-0.0959-0.936j)

### Equations
#### Basic
  Evaluates -> 2x+4 with x -> 2<sup>4</sup>

    import mathpy as mp
    print(mp.equation('x*2+4;2^4'))
                     
    (36+0j)

#### Multiple
  Evaluates -> x<sup>2</sup> + y<sup>2</sup> - 8 with x -> (1+j)<sup>2</sup> and y -> (2-j)

    import mathpy as mp
    print(mp.equation('x^2+y^2+(-8);(1+j)^2,2-j'))

    (-9-4j)

### Roots Finder
#### Durand Kerner Method(all roots)
  Function name -> dk(string, showIter)
  
  string -> 'equation;degree'

  showIter -> Default(False)
              Display all iterations(True)

  Examples

  Find all roots for -> x<sup>2</sup>+2x+1 and degree -> 2

    import mathpy as mp
    print(mp.dk('x^2+2*x+1;2'))

    [(-1-0j), (-1+0j)]

  Find all roots for -> x<sup>2</sup>-2x+1 and degree -> 2

    import mathpy as mp
    print(mp.dk('x^2+(-2)*x+1;2', showIter=True))

    Iterations            root0                  root1
        0            1.0000+0.0000j          0.4000+0.9000j
        1            1.0000+0.0000j          0.4000+0.9000j
        2            1.0000+0.0000j          1.0000+-0.0000j
    [(1+0j), (1-0j)]
  
  Find all roots for -> x<sup>8</sup>+1 and degree -> 8

    import mathpy as mp
    print(mp.dk('x^8+1;8')) 
  
    [(0.38-0.92j), (0.38+0.92j), (-0.92+0.38j), (-0.92-0.38j), (-0.38-0.92j), (0.92-0.38j), (0.92+0.38j), (-0.38+0.92j)]

  Find all roots for -> x<sup>3</sup>-x-2 and degree -> 3

    import mathpy as mp
    print(mp.dk('x^3-x+(-2);3', showIter=True))

    Iterations            root0                  root1                   root2
       0            1.0000+0.0000j          0.4000+0.9000j          -0.6500+0.7200j
       1            1.0000+0.0000j          0.4000+0.9000j          -0.6500+0.7200j
       2            1.1804+1.0111j          -0.8186-1.8992j         -0.3618+0.8880j
       3            1.3050-0.0062j          -0.6449-1.0475j         -0.6602+1.0538j
       4            1.5243-0.0001j          -0.7619-0.8615j         -0.7625+0.8617j
       5            1.5214+-0.0000j         -0.7607-0.8579j         -0.7607+0.8579j
    [(1.52-0j), (-0.76-0.86j), (-0.76+0.86j)]

#### Bisection Method(1 root)  
  Function name -> bm(string, a, b, showIter)

  string -> 'equation'

  a -> value at which equation is +ve or -ve

  b -> value at which equation is -ve or +ve

  showIter -> Default(False)
              Display all iterations(True)

  Example

  Find 1 root for -> x<sup>3</sup>-x-2 in (1, 2)

    import mathpy as mp
    mp.bm('x^3-x+(-2)', a=1, b=2, showIter=True)

    Iterations        a       b       c       cval
      0           1.0000  2.0000  1.5000  -0.1250+0.0000j
      1           1.5000  2.0000  1.7500  1.6094+0.0000j
      2           1.5000  1.7500  1.6250  0.6660+0.0000j
      3           1.5000  1.6250  1.5625  0.2522+0.0000j
      4           1.5000  1.5625  1.5312  0.0591+0.0000j
      5           1.5000  1.5312  1.5156  -0.0341+0.0000j
      6           1.5156  1.5312  1.5234  0.0123+0.0000j
      7           1.5156  1.5234  1.5195  -0.0110+0.0000j
      8           1.5195  1.5234  1.5215  0.0006+0.0000j
      9           1.5195  1.5215  1.5205  -0.0052+0.0000j
      10          1.5205  1.5215  1.5210  -0.0023+0.0000j
      11          1.5210  1.5215  1.5212  -0.0008+0.0000j
      12          1.5212  1.5215  1.5214  -0.0001+0.0000j
    (1.5214+0j)

#### Regula Falsi Method(1 root)  
  Function name -> rf(string, a, b, showIter)

  string -> 'equation'

  a -> value at which equation is +ve or -ve

  b -> value at which equation is -ve or +ve

  showIter -> Default(False)
              Display all iterations(True)

  Example

  Find 1 root for -> x<sup>3</sup>-x-2 in (1, 2)

    import mathpy as mp
    mp.bm('x^3-x+(-2)', a=1, b=2, showIter=True)

    Iterations        a       b       c       f(a)*f(c)
        0           1.0000  2.0000  1.3333  1.9259-0.0000j
        1           1.3333  2.0000  1.4627  0.3210-0.0000j
        2           1.4627  2.0000  1.5040  0.0339-0.0000j
        3           1.5040  2.0000  1.5163  0.0030-0.0000j
        4           1.5163  2.0000  1.5199  0.0003-0.0000j
        5           1.5199  2.0000  1.5210  0.0000-0.0000j
        6           1.5210  2.0000  1.5213  0.0000-0.0000j
    (1.5213+0j)