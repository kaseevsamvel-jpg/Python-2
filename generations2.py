input()
a = [int(x) for x in input().split()]
k = int(input())

for _ in range(k):
    cmd = [int(x) for x in input().split()]
    if cmd[0] == 1:
        a.pop(cmd[1] - 1)
    elif cmd[0] == 2:
        a.insert(cmd[1] - 1, cmd[2])
    elif cmd[0] == 3:
        p = cmd[1]
        a = a[p:] + a[:p]
    else:
        p = cmd[1]
        a = a[-p:] + a[:-p]

print(' '.join(str(x) for x in a))