import random 

def WinCheck (computer_choice, user, moves):
    #if user matches key
    if user == computer_choice:
        print("It's a tie! Nice try!")
    #if user matches value
    elif moves[user] == computer_choice:
        print("You win! Awesome job!")
    #any possibility otherwise
    else :
        print("You lose! Better luck next time!")


def MoveValidation(user) :
    #if user does not match a key/value
    if user not in {"rock", "paper", "scissors"}:
        print("Sorry, that's not a valid move. Please, try again.")
    #return as invalid move
    return False

def Main():
    #set beginning parameter
    pA = True
    #dictionary of moves and beats(keys and values)
    moves = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    #while user wants to play
    while pA == True:
    #intro to game
        print("Welcome to the game!")
        print("Let's play a round of rock, paper, scissors.")
    #allow computer to make random move choice
        computer_choice = random.choice(list(moves))
    #ask user for input
        user = input("Enter your play.")
    #display computer choice
        print("Computer picked: ", computer_choice)
    #when user move is valid
        while MoveValidation(user):
            user = input("Enter your play.")
    #check play for winner
        WinCheck(computer_choice, user, moves)
    #ask user to play again
        new_move = input("Wanna play again? y/n     ")
    #confirm user choice and/or reset game
        if new_move == 'y' :
            pA = True
        else :
            pA == False
            break

#display game play
Main()