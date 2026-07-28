amount_due = 50
sum = 0

while sum < 50:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        amount_due = amount_due - coin
        sum = sum + coin


if sum >= 50:
    print("Change owed:", sum - 50)

