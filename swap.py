a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("a:",a) # Before swapping
print("b:",b)
"""
# Swapping of numbers in traditional way
c = a
a = b
b = c
"""
"""
a = a+b
b = a-b
a = a-b
"""

a,b = b,a  # This way is only applicable in python 
print("a:",a)
print("b:",b)
