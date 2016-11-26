# Mathpy

## Prerequisites
### Python 2 or Python 3
### Install ply using
    pip install ply

## Importing

    import mathpy as mp

### If any error occurs, check order of paranthesis
### Negative numbers should be enclosed in paranthesis
#### Example
  Evaluates -> 1 - 4

    print(mp.cal('1+(-4)'))
    
    (-3+0j)

## Features
### Complex Number Calculation
#### Basic
  Evaluates -> (-4j)

    print(mp.cal('-4j'))
  
    -4j

#### Multiple
  Evaluates -> (2+4j)*(2-8j)+(9-81j)

    print(mp.cal('(2+4j)*(2-8j)+(9-81j)'))

    (45-89j)

#### Power
  Evaluates -> (0.4+0.9j)<sup>4</sup>

    print(mp.cal('(0.4+0.9j)^4'))
  
    (-0.0959-0.936j)

#### Trignometric
  sin, cos, cosec, sec, tan, cot

  Evaluates -> sin(cos((0.4+0.9j)^<sup>2</sup>))

    print(mp.cal('sin(cos((0.4+0.9j)^2))'))

    (0.9447989936113714+0.26124290303222564j)

#### Logarithmic
  ln -> Natural Log

  log -> Log for any base -> log(a, base)

  Evaluates -> log(ln((2+j)^7), 8)

    print(mp.cal('log(ln((2+j)^7), 8)'))

    (2.6780435026876974-0.7134960747558609j)

#### Exponential
  e -> Exponential (e^a)

  Evaluates -> e^(sin((0.1+0.8j)^5))

    mp.cal('e^(sin((0.1+0.8j)^5))')

    (1.181087476388017+0.3331524128924987j)

### Equations
#### Basic
  Evaluates -> 2x+4 with x -> 2<sup>4</sup>

    print(mp.equation('x*2+4;2^4'))
                     
    (36+0j)

#### Multiple
  Evaluates -> x<sup>2</sup>+y<sup>2</sup>-8 with x -> (1+j)<sup>2</sup> and y -> (2-j)

    print(mp.equation('x^2+y^2+(-8);(1+j)^2,2-j'))

    (-9-4j)

#### Combined
  Evaluates -> x<sup>3</sup>+sin(x)+ln(x)+2 with x -> (0.65+8.9j)<sup>2</sup>

    print(mp.equation('x^3+sin(x)+ln(x)+2;(0.65+8.9j)^2'))

    (-444446.119558+162594.208016j)

### Roots Finder
#### Durand Kerner Method(all roots)
  Function name -> dk(string, maxIter, showIter)
  
  string -> 'equation;degree'

  maxIter -> number of Iterations -> Default(100)

  showIter -> Default(False)
              Display all iterations(True)

##### Examples

  Find all roots for -> x<sup>2</sup>+2x+1 and degree -> 2

    print(mp.dk('x^2+2*x+1;2'))

    [(-1-0j), (-1+0j)]

  Find all roots for -> x<sup>2</sup>-2x+1 and degree -> 2

    print(mp.dk('x^2+(-2)*x+1;2', showIter=True))

    Iterations            root0                  root1
        0            1.0000+0.0000j          0.4000+0.9000j
        1            1.0000+0.0000j          0.4000+0.9000j
        2            1.0000+0.0000j          1.0000+-0.0000j
    [(1+0j), (1-0j)]
  
  Find all roots for -> x<sup>8</sup>+1 and degree -> 8

    print(mp.dk('x^8+1;8')) 
  
    [(0.38-0.92j), (0.38+0.92j), (-0.92+0.38j), (-0.92-0.38j), (-0.38-0.92j), (0.92-0.38j), (0.92+0.38j), (-0.38+0.92j)]

  Find all roots for -> x<sup>3</sup>-x-2 and degree -> 3

    print(mp.dk('x^3-x+(-2);3', showIter=True))

    Iterations            root0                  root1                   root2
       0            1.0000+0.0000j          0.4000+0.9000j          -0.6500+0.7200j
       1            1.0000+0.0000j          0.4000+0.9000j          -0.6500+0.7200j
       2            1.1804+1.0111j          -0.8186-1.8992j         -0.3618+0.8880j
       3            1.3050-0.0062j          -0.6449-1.0475j         -0.6602+1.0538j
       4            1.5243-0.0001j          -0.7619-0.8615j         -0.7625+0.8617j
       5            1.5214+-0.0000j         -0.7607-0.8579j         -0.7607+0.8579j
    [(1.52-0j), (-0.76-0.86j), (-0.76+0.86j)]

  Find all roots for -> x<sup>3</sup>+sin(x)+ln(x)+2 and degree -> 3

    mp.dk('x^3+sin(x)+ln(x)+2;3', maxIter=24, showIter=True)

    Iterations            root0                  root1                   root2
       0            1.0000+0.0000j          0.4000+0.9000j          -0.6500+0.7200j
       1            1.0000+0.0000j          0.4000+0.9000j          -0.6500+0.7200j
       2            0.6535-1.9421j          0.2398+3.0048j          -1.1977-1.2777j
       3            0.6814-1.6977j          0.3604+2.3300j          -0.9800-0.4020j
       4            0.5345-1.6266j          0.4408+1.8755j          -0.7994+0.2170j
       5            0.4798-1.6555j          0.4882+1.6925j          -0.9322-0.5140j
       6            0.4590-1.6644j          0.4714+1.6775j          -0.8735+0.3865j
       7            0.4614-1.6697j          0.4651+1.6698j          -0.8660-0.4691j
       8            0.4621-1.6719j          0.4634+1.6710j          -0.8532+0.4298j
       9            0.4626-1.6717j          0.4626+1.6714j          -0.8493-0.4506j
       10           0.4628-1.6717j          0.4627+1.6716j          -0.8457+0.4401j
       11           0.4628-1.6717j          0.4628+1.6717j          -0.8448-0.4459j
       12           0.4628-1.6716j          0.4628+1.6717j          -0.8437+0.4429j
       13           0.4628-1.6716j          0.4628+1.6716j          -0.8435-0.4446j
       14           0.4628-1.6716j          0.4628+1.6716j          -0.8432+0.4438j
       15           0.4628-1.6716j          0.4628+1.6716j          -0.8431-0.4442j
       16           0.4628-1.6716j          0.4628+1.6716j          -0.8430+0.4440j
       17           0.4628-1.6716j          0.4628+1.6716j          -0.8430-0.4441j
       18           0.4628-1.6716j          0.4628+1.6716j          -0.8429+0.4441j
       19           0.4628-1.6716j          0.4628+1.6716j          -0.8429-0.4441j
       20           0.4628-1.6716j          0.4628+1.6716j          -0.8429+0.4441j
       21           0.4628-1.6716j          0.4628+1.6716j          -0.8429-0.4441j
       22           0.4628-1.6716j          0.4628+1.6716j          -0.8429+0.4441j
       23           0.4628-1.6716j          0.4628+1.6716j          -0.8429-0.4441j
    'Not able to find roots'

#### Bisection Method(1 root)  
  Function name -> bm(string, a, b, maxIter, showIter)

  string -> 'equation'

  a -> value at which equation is +ve or -ve

  b -> value at which equation is -ve or +ve

  maxIter -> number of iterations -> Default(100)

  showIter -> Default(False)
              Display all iterations(True)

##### Examples

  Find 1 root for -> x<sup>3</sup>-x-2 in (1, 2)

    mp.bm('x^3-x+(-2)', a=1, b=2, showIter=True)

    Iterations        a       b       c       cval
        0           1.0000  2.0000  1.5000  -0.1250
        1           1.5000  2.0000  1.7500  1.6094
        2           1.5000  1.7500  1.6250  0.6660
        3           1.5000  1.6250  1.5625  0.2522
        4           1.5000  1.5625  1.5312  0.0591
        5           1.5000  1.5312  1.5156  -0.0341
        6           1.5156  1.5312  1.5234  0.0123
        7           1.5156  1.5234  1.5195  -0.0110
        8           1.5195  1.5234  1.5215  0.0006
        9           1.5195  1.5215  1.5205  -0.0052
        10          1.5205  1.5215  1.5210  -0.0023
        11          1.5210  1.5215  1.5212  -0.0008
        12          1.5212  1.5215  1.5214  -0.0001
    1.5214

  Find 1 root for -> x<sup>3</sup>+sin(x)+ln(x)+2 in (0.1, 0.2)

    mp.bm('x^3+sin(x)+ln(x)+2', a=0.1, b=0.2, maxIter=12, showIter=True)

    Iterations        a       b       c       cval
        0           0.1000  0.2000  0.1500  0.2557
        1           0.1000  0.1500  0.1250  0.0472
        2           0.1000  0.1250  0.1125  -0.0711
        3           0.1125  0.1250  0.1187  -0.0106
        4           0.1187  0.1250  0.1219  0.0186
        5           0.1187  0.1219  0.1203  0.0041
        6           0.1187  0.1203  0.1195  -0.0032
        7           0.1195  0.1203  0.1199  0.0004
        8           0.1195  0.1199  0.1197  -0.0014
        9           0.1197  0.1199  0.1198  -0.0005
        10          0.1198  0.1199  0.1199  -0.0000
    0.1199

#### Regula Falsi Method(1 root)  
  Function name -> rf(string, a, b, maxIter, showIter)

  string -> 'equation'

  a -> value at which equation is +ve or -ve

  b -> value at which equation is -ve or +ve

  maxIter -> number of iterations -> Default(100)

  showIter -> Default(False)
              Display all iterations(True)

##### Examples

  Find 1 root for -> x<sup>3</sup>-x-2 in (1, 2)

    mp.rf('x^3-x+(-2)', a=1, b=2, showIter=True)

    Iterations        a       b       c       f(a)*f(c)
        0           1.0000  2.0000  1.3333     1.9259
        1           1.3333  2.0000  1.4627     0.3210
        2           1.4627  2.0000  1.5040     0.0339
        3           1.5040  2.0000  1.5163     0.0030
        4           1.5163  2.0000  1.5199     0.0003
        5           1.5199  2.0000  1.5210     0.0000
        6           1.5210  2.0000  1.5213     0.0000
    1.5213

  Find 1 root for -> x<sup>3</sup>+sin(x)+ln(x)+2 in (0.1, 0.2)

    mp.rf('x^3+sin(x)+ln(x)+2', a=0.1, b=0.2, maxIter=6, showIter=True)

    Iterations        a       b       c       f(a)*f(c)
        0           0.1000  0.2000  0.1253     -0.0100
        1           0.1000  0.1253  0.1203     -0.0008
        2           0.1000  0.1203  0.1199     -0.0001
    0.1199