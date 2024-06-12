#Number Guessing Game Objectives:
from art import logo
print(logo)
import random
print("Welcom to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess_number = random.randint(1, 100)
print(f"Pssst, the correct answer is {guess_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
  attempts = 10
  print("You have 10 attempt to guess the number.") 
elif difficulty == 'hard':
  attempts = 5
  print("You have 5 attempt to guess the number.") 

running = True
while running:
  user_guess = int(input("Make a guess: "))
  if user_guess == guess_number:
    print(f"You got it! The answer was {user_guess}")
    running = False
  elif user_guess != guess_number:
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
    if user_guess > guess_number:
      print("Too high.")
      print("Guess again.")
    elif user_guess < guess_number:
      print("Too low.")
      print("Guess again.")
  elif attempts == 0:
    print("You've run out of guesses, you lose.")
    running = False
