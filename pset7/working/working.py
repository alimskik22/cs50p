import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.search(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    start = convert_time(h1, m1, p1)
    end = convert_time(h2, m2, p2)

    return f"{start} to {end}"



def convert_time(hour, minute, period):
    hour = int(hour)
    minute = 0 if minute is None else int(minute)

    if not (1 <= hour <= 12):
        raise ValueError

    if not (0 <= minute <= 59):
        raise ValueError

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"



if __name__ == "__main__":
    main()
