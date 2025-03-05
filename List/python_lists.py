"""
List is a data type in python where each element is seperated by commas and
enclosed within square brackets
"""
list1 = [45,"Hello",878.45434,True]

#    0    1     2     3
#   -4   -3    -2    -1

# List elements can be accessed using index. And index begins with 0
print("Length of list:", len(list1))
print("Length of list:", list1[len(list1)-1])
print("Length of list:", list1[-1])

print("Elements from 1 to 3:", list1[1:3])
print("Reverse of list:", list1[::-1])

