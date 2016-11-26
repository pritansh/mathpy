import mathpy as mp

#2.0+3.0i
str(mp.cal('2+3i'))

#6.0+6.0i
str(mp.cal('(2+3i)+(4+3i)'))

#2.0+9.0i
str(mp.cal('((1+i)+(-1-i))+(2+9i)'))

#0.0+2.0i
str(mp.cal('(1+i)^(2)'))

#0.9+1.09i
str(mp.cal('(0.9+1.09i)'))

#146.0+0.0i
str(mp.equation('((x)^(2))+(2);12'))

#-9.0-4.0i
str(mp.equation('(((x)^(2))+((y)^(2)))-(8);(1+i)^(2),2-i'))