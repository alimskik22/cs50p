def main():
    fraction = input("Fraction: ")
    result = convert(fraction)
    final_result = gauge(result)
    print(final_result)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x < 0 or y < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    result = round(x / y * 100)

    return result

def gauge(result):
    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return f"{result}%"


if __name__ == "__main__":
    main()
