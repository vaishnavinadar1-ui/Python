months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                break

        elif "," in date:
            month, rest = date.split(" ", 1)

            if month not in months:
                continue

            day, year = rest.split(", ")

            day = int(day)
            year = int(year)

            if not (1 <= day <= 31):
                continue

            month = months.index(month) + 1
            break

    except (ValueError, IndexError):
        pass

print(f"{year}-{month:02}-{day:02}")
