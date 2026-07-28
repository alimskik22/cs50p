import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], "r") as before, open(sys.argv[2], "w") as after:
            fieldnames = ["first", "last", "house"]
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                last_name, first_name = row["name"].split(", ")
                house = row["house"]
                writer.writerow(
                    {"first": first_name, "last": last_name, "house": house}
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
