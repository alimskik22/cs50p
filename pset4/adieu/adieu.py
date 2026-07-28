import inflect

p = inflect.engine()

names = []
count = 1
while True:
    try:
        name = input("Name: ")
        names.append(name)
        count += 1
    except EOFError:
        print()
        break


print("Adieu, adieu, to", p.join(names))
