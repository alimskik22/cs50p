import random


def main():
    level = get_level()

    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        q = str(x) + " + " + str(y) + " = "
        a = input(q)

        tries = 0

        while True:
            if (not a.isdigit() or int(a) != answer) and tries < 2:
                tries += 1
                print("EEE")
                a = input(q)
            elif tries == 2:
                print(q + f"{answer}")
                break

            elif int(a) == answer:
                score += 1
                break

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level not in [1, 2, 3]:
                continue
            else:
                break

    return level


def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
        return integer
    elif level == 2:
        integer = random.randint(10, 99)
        return integer
    elif level == 3:
        integer = random.randint(100, 999)
        return integer
    else:
        raise ValueError


if __name__ == "__main__":
    main()
