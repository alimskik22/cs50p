from random import randint

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level < 0:
            continue
        else:
            break


g = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > g:
            print("Too large!")
            continue
        elif 0 < guess < g:
            print("Too small!")
            continue
        elif guess == g:
            print("Just right!")
            break
        else:
            continue
