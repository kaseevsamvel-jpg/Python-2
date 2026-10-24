input()
marks = sorted(int(x) for x in input().split())

print(sum(marks[1:-1]))