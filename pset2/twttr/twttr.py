inp = input("Input: ")

out = "".join(c for c in inp if c not in "AEIOUaeiou")
print("Output:", out)
