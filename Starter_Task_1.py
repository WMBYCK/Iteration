# William Craddock
# 20/10/2014
# Starter - Task - 1

total = 0
counter = 1

while counter < 6:
    number = int(input("Please enter number {0} in the series: ".format(counter)))
    total = total + number
    counter = counter + 1
    print()
print("The total of the numbers you entered is {0}".format(total))
