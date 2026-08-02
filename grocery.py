grocery = {}

while True:
    try:
        item = input().lower()

        grocery[item] = grocery.get(item, 0) + 1

    except EOFError:
        print()

        for item in sorted(grocery):
            print(grocery[item], item.upper())

        break
