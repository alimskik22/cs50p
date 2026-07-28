def main():
    mass = int(input("Mass: "))
    energy = calcE(mass)
    print(energy)


def calcE(mass):
    energy = mass * pow(300000000, 2)
    return energy


main()
