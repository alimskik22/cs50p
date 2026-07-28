import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    pattern = r"^\d+\.\d+\.\d+\.\d+$"
    if re.search(pattern, ip):
        a, b, c, d = ip.split(".")
        for part in [a, b, c, d]:
            if len(part) > 1 and part.startswith("0"):
                return False
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
