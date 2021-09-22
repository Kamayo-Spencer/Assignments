# Question.
# In plain English and with the Given-required-algorithm table, write a guessing game
# where the user should guess a secret number. After every guess, the problem tells the user whether their number
# was too large or small. In the end, the number of tries  needed should be printed

# Given ifomation
# User should guess a number
# the program prints out whether the number was too large or too small
# The program prints out the number of tries needed

# Required solution
# Get input from the user( should be a number)
# print out whether the number is too big or too small
# print out the numbers of attempts needed.

# Algorithm
from random import randint

no1 = randint(1 , 100)
for i in range(1,4):
    no = int(input("Guess a random number between 1 and 100 :"))
    if no > no1:
        print("Your no is too large")
    elif no < no1:
        print("Your number is too small")
    else:
        print(f"You are good at guessing.  The number is {no1}")
    
    if i == 3:
        print("Sorry, you only had three tries")


