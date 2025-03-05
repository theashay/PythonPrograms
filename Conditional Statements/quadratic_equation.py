"""
-b+sqrt(b2-4ac)/2a
-b+sqrt(b2-4ac)/2a
"""

import math

a = int(input("Enter the coefficient of x2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the coefficient of term: "))
dis = (b*b) - (4*a*c)
print("Discriminant = ", dis)

if dis==0:
    print("Both roots are equal")
    r1 = r2 = (-b + math.sqrt(dis))/(2*a)
    print("Root1: ", r1, "Root2: ", r2)
elif dis>0:
    print("Both roots are real")
    r1 = (-b + math.sqrt(dis))/(2*a)
    r2 = (-b - math.sqrt(dis))/(2*a)
    print("Root1: ", r1, "Root2: ", r2)
else:
    print("Both roots are complex")
    
