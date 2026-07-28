def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if starts_w_two_letters(s) and max_min(s) and no_punct(s) and nums(s):
        return True
    else:
        return False


def max_min(plate):
    if 2 <= len(plate) <= 6:
        return True
    return False


def starts_w_two_letters(plate):
    if plate[0:2].isalpha():
        return True
    return False


def no_punct(plate):
    for c in plate:
        if not(c.isalpha()) and not(c.isdigit()):
            return False
    return True


def nums(plate):
    for i, c in enumerate(plate):
        if c.isdigit():
            if c == "0":
                return False
            for remaining in plate[i : ]:
                if not remaining.isdigit():
                    return False
            return True
    return True



if __name__ == "__main__":
    main()
