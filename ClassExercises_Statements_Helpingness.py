# William Craddock
# 22/10/2014
# Class Exercises - Statements - Helpingness

#prints Hello 9 times
for count in range (1,10):
    print("Hello")

#keeps prompting the user until they enter a number between 1 and 10
valid = False
while not valid:
    number = int(input("Enter a number in the range 1 to 10:"))
    if 1 <= number <= 10:
        valid = True
