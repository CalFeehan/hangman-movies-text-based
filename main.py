from random import randint
import re

# win/loss tracker
wins = 0
losses = 0


def gather_input():
    """
    Gather user input as a lowercase string. This will only accept one character a-z or A-Z.

    :param:
    :return: string input_guess
    """
    while True:
        input_guess = (input("Please enter your next guess: "))
        input_guess = input_guess.lower()
        if re.search('^[a-zA-Z]$', input_guess):
            break
        print('One letter, a-z please.')
        continue
    return input_guess


def check_string(guess):
    """
    Checks if player guess is correct. If correct modify left_to_guess, else removes one life.
    Appends the guess to previous_guess list.
     :param guess: 1 char str of users guess
    :return:
    """
    global left_to_guess
    global lives
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                left_to_guess = left_to_guess[:i] + guess + left_to_guess[i+1:]
    else:
        lives -= 1

    previous_guesses.append(guess)


def play_again():
    """
    Asks the user if they would like to play again. Accepts y/Y/n/N as input from user.

    :param:
    :return: True or False
    """
    while True:
        choice = input("Play again? (Y/N): ")
        if re.search('^[yY]$', choice):
            return True
        elif re.search('^[nN]$', choice):
            return False
        print('Y/N')
        continue


while True:
    # variables inside while loop to re-instantiate them if player continues
    left_to_guess = str()
    lives = 7
    previous_guesses = list()

    # open file, choose random line, make lowercase, converts word to ______ format
    with open("movie_list.txt", mode="r") as file:
        all_words = file.readlines()
        word = (all_words[randint(0, 76)])
        word = word.lower()
        file.close()
        for x in range(len(word)-1):
            left_to_guess += '_'

        # checks for spaces and removes '_'. j used as counter, can't figure out how to use string index.
        j = 0
        for letter in word:
            if letter == ' ':
                left_to_guess = left_to_guess[:j] + ' ' + left_to_guess[j+1:]
            j += 1

    # while the user has lives and there are still blanks: tells the user how many guesses left and previous guesses.
    # prints hangman _____ and calls check_string on gather_input.
    while lives > 0 and '_' in left_to_guess:
        print(f'Lives left: {lives}, Previous guesses:', previous_guesses)
        print(left_to_guess)
        check_string(gather_input())
        continue

    # if the player loses it will tell them the correct answer and add 1 to loss counter,
    # if they win it adds 1 to win counter.
    if lives == 0:
        print(f'You Lose! :( The answer was {word.title()}')
        losses += 1
    else:
        print('Winner!')
        wins += 1

    # prints the players scoreboard
    print(f'Wins: {wins}, Losses: {losses}')

    # checks if the user wants to play again, if so deletes variables allowing them to be re-instantiated.
    if play_again():
        del word
        del all_words
        del left_to_guess
        continue
    break
