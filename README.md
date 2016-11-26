# Mathpy

## Prerequisites
### Python 2
### Install ply using
    pip install ply

## If any error occurs, check order of paranthesis

## Features
### Complex Number Calculation
#### Basic
    import mathpy as mp
    str(mp.cal('-4i'))
  evaluates -> (-4i)

  prints -> 0.0-4.0i
#### Multiple
    import mathpy as mp
    str(mp.cal('((2+4i)*(2-8i))+(9-81i)'))
  evaluates -> (2+4i)*(2-8i)+(9-81i)

  prints -> 45.0-89.0i
#### Power
    import mathpy as mp
    str(mp.cal('(0.4+0.9i)^(4)'))
  evaluates -> (0.4+0.9i)<sup>4</sup>

  prints -> -0.0959-0.936i

### Equations
#### Basic
    import mathpy as mp
    str(mp.equation('((x)*(2))+(4);(2)^(4)'))
  evaluates -> x<sup>2</sup>+4 with x -> 2<sup>4</sup>
                     
  prints -> 36.0
#### Multiple
    import mathpy as mp
    str(mp.equation('(((x)^(2))+((y)^(2)))-(8);(1+i)^(2),2-i'))
  evaluates -> x<sup>2</sup> + y<sup>2</sup> - 8 with x -> (1+i)<sup>2</sup> and y -> (2-i)
                     
  prints -> -9.0-4.0i