s1 = "HelloPython"
print(s1)

print(s1.upper())  # upper is a method
print(len(s1))     # len is a function

"""
ASCII code
A-65  B-66  Z-90
a-97  b-98  c-99  d-100  e-101  z-122
0-48  1-49  2-50  9-58
space( ) - 32
"""

print(max(s1))     # returns value with highest ASCII code
print(min(s1))     # returns value with lowest ASCII code

print(ord(s1[1]))  # ord function returns the ASCII code of specified character

print(chr(97))     # returns the ASCII value of that ASCII code

print(s1.casefold())  # converts the string in lowercase
print(s1.swapcase())  # swaps lowercase into uppercase and vice versa

print(s1.isalnum())  # returns True as s1 string contains alphabetical characters
print(s1.isdigit())  # returns False as s1 string does not contain numeric characters

