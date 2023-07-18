import random
import math

def guess_num(lower, upper):
    num = random.randint(lower, upper)
    minimum_guesses = math.ceil(math.log(upper - lower + 1, 2))

    print("Think of a number between", lower, "and", upper)

    for count in range(1, minimum_guesses + 1):
        guess = random.randint(lower, upper)
        
        print("Computer's guess:", guess)

        if guess == num:
            print("The computer guessed it in", count, "tries!")
            return

        if guess < num:
            print("Too small!")
            lower = guess + 1
        else:
            print("Too large!")
            upper = guess - 1

    print("The computer failed to guess within the minimum number of guesses.")

smaller_num = int(input("Enter the smaller number: "))
larger_num = int(input("Enter the larger number: "))

guess_num(smaller_num, larger_num)
