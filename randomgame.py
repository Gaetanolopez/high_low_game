import random

random_number = random.choice(range(101))

def game(guess_choice):
    return int(guess_choice)

def high_low(random):
    if guess == random:
        return "correct"
    elif guess < random:
        print("too low")
    elif guess > random:
        print("too high")

def game_mode(difficulty):
    if difficulty == "simple":
        return 10
    elif difficulty == "hard":
        return 5

game_on = True
while game_on:
    play_high_low = input("Do you want to play high_low? y or n")
    if play_high_low == "y":
        level = game_mode(input("Chooose a difficulty: simple , hard"))
        while level > 0:
            guess = game(input("Guess number from 1 to 100"))
            win = high_low(random_number)
            level = level - 1
            print(f"You have {level} attempts left")
            if win == "correct":
                print("you win")
                break
            if level == 0:
                print(f"you loose, secret number was {random_number}")

    elif play_high_low == "n":
        game_on = False





