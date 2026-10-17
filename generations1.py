input()
a = [int(x) for x in input().split()]
k = int(input())

for _ in range(k):
    cmd = [int(x) for x in input().split()]
    if cmd[0] == 1:
        a.pop(cmd[1] - 1)
    elif cmd[0] == 2:
        a.insert(cmd[1] - 1, cmd[2])
    else:
        i, j = cmd[1] - 1, cmd[2] - 1
        a[i], a[j] = a[j], a[i]

print(' '.join(str(x) for x in a))