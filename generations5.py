input()
a = [int(x) for x in input().split()]

smallest = min(a)
second = min(x for x in a if x != smallest)

print(second, a.index(second) + 1)