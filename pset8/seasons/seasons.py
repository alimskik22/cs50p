from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    try:
        bd = date.fromisoformat(input("Date of birth: "))
    except ValueError:
        sys.exit("Invalid date")
    else:
        today = date.today()
        minutes = minutes_since(today, bd)
        result = to_words(minutes)
        print(result)


def minutes_since(today, bd):
    return (today - bd).days * 24 * 60


def to_words(minutes):
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()
