import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        numbers = ip.split(".")

        for num in numbers:

            if len(num) > 1 and num.startswith("0"):
                return False

            if int(num) < 0 or int(num) > 255:
                return False

        return True

    return False


if __name__ == "__main__":
    main()
