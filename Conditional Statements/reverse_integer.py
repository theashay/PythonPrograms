no = int(input("Enter any number:"))
# print(no)
no=str(no)
revno = (no[::-1])

if no==revno:
    print("Palindrome")
else:
    print("Not Palindrome")
