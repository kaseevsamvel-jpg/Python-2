n, m = [int(x) for x in input().split()]

matrix = []
for _ in range(n):
    row = [random.randint(1, 10) for _ in range(m)]
    matrix.append(' '.join(str(x) for x in row))
    print (*matrix[-1])

input()
cols = [int(x) - 1 for x in input().split()]

for row in matrix:
    print(' '.join(row[c] for c in cols))