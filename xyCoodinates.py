
from math import sin, cos
for degrees in (0,30,60,90,120,150,180,210,240,270,300,330):
    radians = degrees * 0.01745329252
    print(degrees,"1 UNIT X=",round(cos(radians)),"Y=",round(sin(radians)),"\t UNITS X=",round(cos(radians)*2),"Y=",round(sin(radians)*2) )
