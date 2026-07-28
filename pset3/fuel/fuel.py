while True:
    fraction = input("Fraction: ")

    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x < 0 or y <= 0:
            continue
        if x > y:
            continue

        result = round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break


if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")
