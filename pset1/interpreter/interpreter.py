def main():
    exp = input("Expression: ")

    x, y, z = exp.split(" ")

    if y == "+":
        result = float(x) + float(z)
        printFormattedResult(result)
    elif y == "-":
        result = float(x) - float(z)
        printFormattedResult(result)
    elif y == "*":
        result = float(x) * float(z)
        printFormattedResult(result)
    else:
        result = float(x) / float(z)
        printFormattedResult(result)



def printFormattedResult(result):
    print(f"{hours, minutes = time.split(":")}")


main()
