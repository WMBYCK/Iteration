# William Craddock
# 04/11/2014
# Class Exercise - Revision Exercise - Task 3

total = 0
number = 0
numofnum = int(input("Please enter how many numbers you would like to enter: "))
for count in range(numofnum):
    number = int(input("Please enter number: "))
    total = total + number
answer = total / numofnum
print("The average of these numbers is {0}".format(answer))
