# Number-Guessing-Game
A Python number guessing game where players guess a number between 1-100 with limited attempts based on chosen difficulty.

'''
  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    T|  T  T  /  _]/ ___// ___/    |      T|  T  T  /  _]    |    \ |  T  T|   T   T|    \   /  _]|    \ 
Y   __j|  |  | /  [_(   \_(   \_     |      ||  l  | /  [_     |  _  Y|  |  || _   _ ||  o  ) /  [_ |  D  )
|  T  ||  |  |Y    _]\__  T\__  T    l_j  l_j|  _  |Y    _]    |  |  ||  |  ||  \_/  ||     TY    _]|    / 
|  l_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     |l     ||     T\    |\    |      |  |  |  |  ||     T    |  |  |l     ||   |   ||     ||     T|  .  Y
l___,_j \__,_jl_____j \___j \___j      l__j  l__j__jl_____j    l__j__j \__,_jl___j___jl_____jl_____jl__j\_j

'''
# Number Guessing Game

A simple Python number guessing game where the player has to guess a randomly generated number within a specified range and a limited number of attempts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)


## Overview

Welcome to the Number Guessing Game! The objective is to guess the number chosen by the computer between 1 and 100. You can choose the difficulty level which determines the number of attempts you have to guess the number.

## Features

- Choose between 'easy' or 'hard' difficulty levels.
  - Easy: 10 attempts
  - Hard: 5 attempts
- Provides feedback whether the guess is too high or too low.
- Displays the number of attempts remaining.


## Usage

1. **Run the game**
    ```sh
    python main.py
    ```

2. **Follow the prompts**
    - The game will prompt you to choose a difficulty level.
    - After selecting the difficulty, you will have a limited number of attempts to guess the correct number.
    - Enter your guesses and follow the feedback provided.

Example:

```plaintext
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
...
