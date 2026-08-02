from datetime import date
import inflect
import sys

p = inflect.engine()


def convert(birth):
    today = date.today()
    difference = today - birth
    minutes = difference.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


def main():
    birthday = input("Date of Birth: ")

    try:
        birth = date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Invalid date")

    print(convert(birth))


if __name__ == "__main__":
    main()
