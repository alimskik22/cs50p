def main():
    inp = input("Input: ")
    out = shorten(inp)
    print("Output:", out)


def shorten(word):
    out = "".join(c for c in word if c not in "AEIOUaeiou")
    return out


if __name__ == "__main__":
    main()
