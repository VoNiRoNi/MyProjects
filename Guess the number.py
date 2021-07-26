import random


def GuessTheNumber():
    print("Try to guess number which I made a wish for. This number located between one and fifty")
    number = random.randint(0, 51)
    while True:
        numberPlayer = int(input())
        if numberPlayer < number:
            print("You're wrong. Your number is less than I guessed")
        elif numberPlayer > number:
            print("You're wrong. Your number is more than I guessed")
        elif number == numberPlayer:
            print("You're right! You guessed the number.")
            break


if __name__ == '__main__':
    GuessTheNumber()
