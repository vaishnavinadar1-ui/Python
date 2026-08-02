def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Rule 1: Length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 3: No punctuation or spaces
    if not s.isalnum():
        return False

    number_started = False

    for char in s:

        # If character is a number
        if char.isdigit():

            # First number cannot be 0
            if not number_started:
                if char == "0":
                    return False

            number_started = True

        # If letter comes after number → invalid
        else:
            if number_started:
                return False

    return True


main()
