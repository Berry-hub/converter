# hra rock / paper / scissors

from random import choice
#
print("Let's play!" + "\n"
+ "You choose 'r' for rock, 'p' for paper or 's' for scissors." + "\n"
+ "Game has 5 rounds, the one winning more of them is a winner.")
#
def game():
    no_of_rounds = 1
    your_winning_rounds = 0
    comp_winning_rounds = 0
    while no_of_rounds <= 5:
        print("Round number: ", no_of_rounds)
        your_choice = input("What is you choice? Write: 'r', 'p' or 's': ")
        list_of_choices = ["rock", "paper", "scissors"]
        computer_choice = choice(list_of_choices)
        if your_choice == 'r' or your_choice == 'p' or your_choice == 's':
            print("Computer: ", computer_choice)
        else:
            print("I don't understand your choice, write: 'r', 'p' or 's': ")
            no_of_rounds += 0
        if (your_choice == 'r' and computer_choice == 'rock') or (your_choice == 'p' and computer_choice == 'paper') or (your_choice == 's' and computer_choice == 'scissors'):
            print("Draw!")
            no_of_rounds += 1
        elif (your_choice == 'r' and computer_choice == 'scissors') or (your_choice == 'p' and computer_choice == 'rock') or (your_choice == 's' and computer_choice == 'paper'):
            print("This round for you!")
            no_of_rounds += 1
            your_winning_rounds += 1
        elif (your_choice == 'r' and computer_choice == 'paper') or (your_choice == 'p' and computer_choice == 'scissors') or (your_choice == 's' and computer_choice == 'rock'):
            print("This round for computer!")
            no_of_rounds += 1
            comp_winning_rounds += 1

    print("RESULT")
    print("Rounds for you: ", your_winning_rounds)
    print("Rounds for computer: ", comp_winning_rounds)
    print("Draw rounds: ", (no_of_rounds - (your_winning_rounds + comp_winning_rounds + 1)))
    if your_winning_rounds > comp_winning_rounds:
        print("You're a winner!")
    elif your_winning_rounds < comp_winning_rounds:
        print("You lost, computer is a winner!")
    elif your_winning_rounds == comp_winning_rounds:
        print("Draw!")
    
game()
