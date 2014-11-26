guessed = False
noOfTurns = 0
import random
number=random.randint(1,100)
while not guessed:
    noOfTurns = noOfTurns + 1
    userGuess = int(input("Enter your guess for the number: "))
    if userGuess == number:
        guessed = True
    elif userGuess > number:
        print("The number you guessed is too high")
    else:
        print("The number you guessed is too low")
print("You took {0} turns to guess the number. The Number was {1}".format (noOfTurns,number))
