import random

random_num = random.randint(1, 100)

while True:
    num = int(input("Pick a number (between 1 and 100): "))

    if num > random_num:
        print("go lower")
    elif num < random_num:
        print("go higher")
    else:
        print("congrats!")
        break
