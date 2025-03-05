s1 = "Hello World"
#     -11
# s1 = H e l l o   W o r l d
#      0 1 2 3 4 5 6 7 8 9 10

print(s1)
print("Length:",len(s1))
print("Character at 0th index:",s1[0])
print("Character at 7th index:",s1[7])

# String Slicing
# s1[startindex:endindex]

print("Slicing from 2 to 8:",s1[2:8])
print("Slicing from 1 to 9 with step 2:",s1[1:9:2])

# if end index is not given, it will print upto last character
print("Slicing from 2:",s1[2:])

# if start index is not given, it will print from 0th index
print("Slicing till 8:",s1[:8])

print(s1[9:1:-1])
print("Reverse:",s1[::-1])

