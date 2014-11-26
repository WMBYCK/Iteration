number = int(input("Please enter an integer : "))
print("Times table for {0}:".format (number))
for count in range (1,13):
    answer = count * number
    print("{0:>2} * {1:<2} = {2:>3}".format (count,number,answer))
