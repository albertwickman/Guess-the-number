from random import randrange
from math import fabs


def tryNumber(user):
    while True:
        try:
            n = int(input(user + " bet: "))
        except ValueError:
            pass
        else:
            if n in range(0, 101):
                return n
def computerGuess():
    randomGuess = randrange(0, 101)
    return randomGuess


def main():
    user1Guess = tryNumber("User 1")
    user2Guess = tryNumber("User2")

    randompicked = computerGuess()

    u1diff = fabs(randompicked - user1Guess)
    u2diff = fabs(randompicked - user2Guess)

    valid_answer_yes = "Yes"
    valid_answer_no = "No"

    if u1diff == u2diff:
        print("Tie")
    elif u1diff < u2diff:
        print("User 1 won. The number was: "+str(randompicked))
    else:
        print("User 2 won. The number was: "+str(randompicked))

    redo = input("Do you want to play again? ")
    if redo in valid_answer_yes:
        main()
    elif redo in valid_answer_no:
        print("The game has been terminated...")
        exit()


main()
