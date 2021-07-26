import random
import time


def Game():
    print(
        'Info: Two-four Players can play in this game.Three dice are thrown, the player who has the sum of the '
        'dropped points equal to one of the two numbers named by him before the start of the game  - wins. For '
        'example, '
        'a player called 7 and 13, and one of his successful throws is shown in the figure.')
    colplayers = int(input("Enter the number of players: "))
    numberToWin = {}
    players = []
    for player in range(1, colplayers + 1):
        players.append(input(f"Enter the name of player number {player}:"))
        num1 = int(input("Enter the first number that should fall out for you to win: "))
        num2 = int(input("Enter the second number that should fall out for you to win: "))
        name = players[player - 1]
        numberToWin[name] = num1, num2
    print("Now I will roll three dice")
    print("Rolling...")
    time.sleep(4)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    print(f"The first dice : {dice1}")
    time.sleep(1)
    print(f"The second dice : {dice2}")
    time.sleep(1)
    print(f"The third dice : {dice3}")
    sumDices = dice1 + dice2 + dice3
    print(f"Sum = {sumDices}")
    time.sleep(0.500)
    for name in players:
        sums = numberToWin[name]
        for r in sums:
            if r == sumDices:
                print(f"{name} win this game!")
                return 0
    print("No one could guess the sum of the dice :(. Try again!")


if __name__ == '__main__':
    Game()
