def main():
    greet = input("Greeting: ")

    result = value(greet)
    print(f"${result}")


def value(greet):
    greet = greet.lower().strip()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h") and greet != "hello":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
