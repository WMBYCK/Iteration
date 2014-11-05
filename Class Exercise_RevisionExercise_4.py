# William Craddock
# 04/11/2014
# Class Exercise - Revision Exercise - Task 4

valid = False
while not valid:
    number = int(input("Enter a number in the range 10 to 20:"))
    if 10 <= number <= 20:
        valid = True
    else:
        print("Sorry that is not in the range, Please try again")
