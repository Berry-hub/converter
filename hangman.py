from random import choice
from hangman_picture import picture

def hangman():
    list_of_czech_words = ["stromek", "krava", "mandolina", "konvalinka"]
    list_of_english_words = ["computer", "keyboard", "chair", "curtains", "pizza", "calculator", "table", "puzzle", "kitchen",
    "dwarves", "jazz", "funny", "pyjamas", "syndrome", "vodka", "drummer", "galaxy", "buffalo", "yachtsman", "scratch", "oxygen",
    "competition", "distributor", "responsible", "observation"]
    word = choice(list_of_english_words)
    unsuccesful_round = 0
    new_word = "_" * len(word)
    print("We start, guess a word: ", new_word)
    while unsuccesful_round < 10:
        guess = input("guess a letter: ").lower()
        if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Bad guess, you can guess 1 letter at one time!")
        else:
            if guess in word:
                position = word.index(guess)
                first_part = new_word[:position]
                second_part = new_word[position+1:]
                if word.count(guess) == 1:
                    new_word = first_part + guess + second_part
                elif word.count(guess) == 2:
                    second_position = word.index(guess,position+1)
                    second_part = new_word[position+1:second_position]
                    third_part = new_word[second_position+1:]
                    new_word = first_part + guess + second_part + guess + third_part
                print(new_word.upper())
                unsuccesful_round += 0
                if new_word == word:
                    print(f'Congratulations, you won! You are safe!')
                    break
            elif guess not in word:
                print("word does not contain this letter ", new_word.upper())
                unsuccesful_round += 1
                print(picture(unsuccesful_round))
                if unsuccesful_round == 10:
                    print("You lost, you are hanging! The answer was", word.upper())

def hangman_game():
    while True:
        answer = input("Do you wanna play hangman? Answer Y/N: ")
        if answer.upper() == "N":
            break
        elif answer.upper() == "Y":
            hangman()
        else:
            print("I don't understand your choice!")

hangman_game()