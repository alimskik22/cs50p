grocery = {}

while True:
    try:
        item = input()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except EOFError:
        print()
        break
    except KeyError:
        pass



for item in sorted(grocery):
    print(grocery[item], item.upper())
