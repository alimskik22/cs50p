import sys

right_lines = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        for line in lines:
            if line.lstrip().startswith("#"):
                continue
            elif line.strip() == "":
                continue
            else:
                right_lines.append(line)


print(len(right_lines))
