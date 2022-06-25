import math

a= 1
b= 3
c= -4

delta = ( b**2 ) - ( 4*a*c ) 
delta = math.sqrt(delta)

x1 = (-b+ delta ) / ( 2*a )
x2 = ( -b- delta )/( 2*a )

print ("x' = " , x1)
print ("x'' = " , x2)