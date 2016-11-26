# Mathpy

## Prerequisites
### Python 2 or Python 3
### Install ply using
    pip install ply

## If any error occurs, check order of paranthesis
## Negative numbers should be enclosed in paranthesis
### Examples
    import mathpy as mp
    mp.cal('1+(-4)')
  evaluates -> 1 - 4
    
  prints -> -3+0j

## Features
### Complex Number Calculation
#### Basic
    import mathpy as mp
    mp.cal('-4i')
  evaluates -> (-4i)

  prints -> -4j
#### Multiple
    import mathpy as mp
    mp.cal('(2+4i)*(2-8i)+(9-81i)')
  evaluates -> (2+4i)*(2-8i)+(9-81i)

  prints -> 45-89j
#### Power
    import mathpy as mp
    mp.cal('(0.4+0.9i)^4')
  evaluates -> (0.4+0.9i)<sup>4</sup>

  prints -> -0.09590000000000004-0.9360000000000002j

### Equations
#### Basic
    import mathpy as mp
    mp.equation('x*2+4;2^4')
  evaluates -> 2x+4 with x -> 2<sup>4</sup>
                     
  prints -> 36+0j
#### Multiple
    import mathpy as mp
    mp.equation('x^2+y^2+(-8);(1+i)^2,2-i')
  evaluates -> x<sup>2</sup> + y<sup>2</sup> - 8 with x -> (1+i)<sup>2</sup> and y -> (2-i)
                     
  prints -> -9-4j