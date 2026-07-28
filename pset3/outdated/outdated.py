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
        inp = input("Date: ")

        if "/" in inp:
            month, day, year = inp.split("/")
        else:
            month, day, year = inp.split()

            if not day.endswith(","):
                continue
                
            day = day.rstrip(",")
            month = months.index(month) + 1

        month = int(month)
        day = int(day)
        year = int(year)

        if not (1 <= month <= 12):
            continue
        if not (1 <= day <= 31):
            continue

        print(f"{year}-{month:02}-{day:02}")
    except (ValueError, IndexError):
        continue
    else:
        break

