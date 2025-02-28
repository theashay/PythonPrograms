# Write a python program to accept a number to print
# whether it is 1 digit, 2 digit, 3 digit, or more than 3 digit number

num = int(input("Enter the number: "))
if num>=1 and num<=9:
    print("This is 1 digit number")
else:
    if num>=10 and num<=99:
        print("This is 2 digit number")
    else:
        if num>=100 and num<=999:
            print("This is 3 digit number")
        else:
            print("More than 3 digit")
            
