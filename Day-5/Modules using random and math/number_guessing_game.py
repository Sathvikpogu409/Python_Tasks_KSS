#Create a Number Guessing Game where: 
#● The program generates a random number between 1 and 50 using random. 
#● The user has 5 attempts to guess the number. 
#● After each guess, calculate the absolute difference using math.fabs() and 
#display how far the guess is from the correct number.

import random
import math

secret_number = random.randint(1, 50)

attempts = 5
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 5 attempts.")

for i in range(1, attempts + 1):

    guess = int(input(f"\nAttempt {i}: Enter your guess: "))

    difference = math.fabs(secret_number - guess)

    print("You are", difference, "away from the correct number.")

    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif i == attempts:
        print("Sorry! You have used all your attempts.")
        print("The correct number was:", secret_number)
    elif guess < secret_number:
        print("Hint: Try a higher number.")
    else:
        print("Hint: Try a lower number.")
