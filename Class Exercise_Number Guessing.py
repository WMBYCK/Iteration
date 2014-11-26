import random
number = random.randint(0,100)
#print(number)
count = 0
valid = False
while not valid:
    guess = int(input("Please enter a guess: "))
    if guess == number:
        count = count + 1
        valid = True
        print("That's the number, it took you {0} guesses".format(count))
    elif 1 <= guess < number:
        count = count + 1
        print("That's not the number, it's too low")
    elif number < guess <= 100:
        count = count + 1
        print("That's not the number, it's too high")
    else:
        print("That is out the range, remember it's 1 to 100")
