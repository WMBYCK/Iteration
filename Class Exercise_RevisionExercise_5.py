# William Craddock
# 04/11/2014
# Class Exercise - Revision Exercise - Task 5

counter = 1
number = 1
total = 0
while number != -1:
    number = int(input("Please enter number"))
    if number > 0:
        total = total + number
        total = total / counter
        counter = counter + 1
print(total)
