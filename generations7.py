import random

n, m = [int(x) for x in input().split()]

matrix = []
for _ in range(n):
    row = [random.randint(1, 10) for _ in range(m)]
    matrix.append(' '.join(str(x) for x in row))
    print (*matrix[-1])

input()
rows = [int(x) - 1 for x in input().split()]

print('\n'.join(matrix[r] for r in rows))