# William Craddock
# 22/10/2014
# Class Exercises - Statements - Addition

number = 0
for count in range (1,9):
    num = int(input("Enter Number {0} : ".format (count)))
    number = number + num
print("The total is {0}.".format(number))
