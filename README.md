# Mathpy

## Prerequisites
### Python 2 or Python 3
### Install ply using
    pip install ply

## If any error occurs, check order of paranthesis
## Negative numbers should be enclosed in paranthesis
### Examples
    import mathpy as mp
    print(mp.cal('1+(-4)'))
  evaluates -> 1 - 4
    
  prints -> (-3+0j)

## Features
### Complex Number Calculation
#### Basic
    import mathpy as mp
    print(mp.cal('-4j'))
  evaluates -> (-4j)

  prints -> -4j
#### Multiple
    import mathpy as mp
    print(mp.cal('(2+4j)*(2-8j)+(9-81j)'))
  evaluates -> (2+4j)*(2-8j)+(9-81j)

  prints -> (45-89j)
#### Power
    import mathpy as mp
    print(mp.cal('(0.4+0.9j)^4'))
  evaluates -> (0.4+0.9j)<sup>4</sup>

  prints -> (-0.0959-0.936j)

### Equations
#### Basic
    import mathpy as mp
    print(mp.equation('x*2+4;2^4'))
  evaluates -> 2x+4 with x -> 2<sup>4</sup>
                     
  prints -> (36+0j)
#### Multiple
    import mathpy as mp
    print(mp.equation('x^2+y^2+(-8);(1+j)^2,2-j'))
  evaluates -> x<sup>2</sup> + y<sup>2</sup> - 8 with x -> (1+j)<sup>2</sup> and y -> (2-j)
                     
  prints -> (-9-4j)

### Roots Finder
#### All roots (Durand Kerner)
  Function name -> dk(string, showIter)
  
  string -> 'equation;degree'
  showIter -> Default(False)
              Display all iterations(True)

  Examples

    import mathpy as mp
    print(mp.dk('x^2+2*x+1;2'))
  find roots for -> x<sup>2</sup>+2x+1 and degree -> 2

  prints -> [(-1-0j), (-1+0j)]

    import mathpy as mp
    print(mp.dk('x^2+(-2)*x+1;2', showIter=True))
  find roots for -> x<sup>2</sup>-2x+1 and degree -> 2

  prints ->
  
    Iterations            root0                  root1
        0            1.0000+0.0000j          0.4000+0.9000j
        1            1.0000+0.0000j          0.4000+0.9000j
        2            1.0000+0.0000j          1.0000+-0.0000j
  [(1+0j), (1-0j)]
  
    import mathpy as mp
    print(mp.dk('x^8+1;8'), show)
  find roots for -> x<sup>8</sup>+1 and degree -> 8

  prints -> [(0.38-0.92j), (0.38+0.92j), (-0.92+0.38j), (-0.92-0.38j), (-0.38-0.92j), (0.92-0.38j), (0.92+0.38j), (-0.38+0.92j)]