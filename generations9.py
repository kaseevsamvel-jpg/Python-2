import random

n, m = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(n)]
matrix = []
for _ in range(n):
    row = [random.randint(1, 10) for _ in range(m)]
    matrix.append(row)
    print("".join(f"{x:3d}" for x in matrix[-1]))
input()
rows = [int(x) - 1 for x in input().split()]
input()
cols = [int(x) - 1 for x in input().split()]

for r in rows:
    for c in cols:
        print(matrix[r][c], end=" ")
    print()