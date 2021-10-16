import random
def guess_game():
    chosen_number= int(random.random()*500)

    guess = int(input(" please guess :"))

    while guess != chosen_number:
        if guess < chosen_number:
            print("the number is higher !")
            guess = int(input(" please guess again :"))
        elif guess > chosen_number:
            print("the number is lower !")
            guess = int(input(" please guess again :"))

    else :
        print (" you guessed the right number hooray!")



