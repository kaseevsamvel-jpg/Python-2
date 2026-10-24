import random

n, m = [int(x) for x in input().split()]

matrix = []
for _ in range(n):
    row = [random.randint(1, 10) for _ in range(m)]
    matrix.append(' '.join(str(x) for x in row))
    print (*matrix[-1])

k = int(input())

for row in matrix[-k:] + matrix[:k]:
    print(row)