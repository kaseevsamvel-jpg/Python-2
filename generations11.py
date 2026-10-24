import random

n, m = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(n)]
matrix = []
for _ in range(n):
    row = [random.randint(1, 10) for _ in range(m)]
    matrix.append(row)
    print(''.join(F'x{x:3d}' for x in matrix[-1]))
k = int(input())

LAST = slice(-k, None)
FIRST = slice(None, k)

for part in (LAST, FIRST):
    for row in matrix[part]:
        print(''.join(F'x{x:3d}' for x in row[part]))
