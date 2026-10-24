input()
incomes = [int(x) for x in input().split()]
taxes = [int(x) for x in input().split()]

amounts = [v * p for v, p in zip(incomes, taxes)]

print(amounts.index(max(amounts)) + 1)