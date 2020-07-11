"""A number-guessing game."""

import random
chosen_number = random.randrange(101) 

greeting = input("Hello! What is your name? ") 

print("Hi, {greeting}! I'm thinking of a number between 1 and 100.".format(greeting = greeting))

number_guess = input("Try to guess what number I'm thinking! ")

if int(number_guess) == int(chosen_number):
    print("Wow! You guessed it! You got it on the first try!")

tries = 0    

while int(number_guess) != int(chosen_number):


    if int(number_guess) > int(chosen_number):
        tries += 1
        number_guess = input("Your guess is too high. Try again!" )
          

    if int(number_guess) < int(chosen_number):
        tries += 1
        number_guess = input("Your guess is too low. Try again! ") 
        

print("Wow! You guessed it! You got it in {tries} tries!".format(tries = tries))
