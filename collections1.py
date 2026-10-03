number = int(input())
list_A = [int(x) for x in input().split()]

for _ in range(2):
    print(" ".join(str(x) for x in list_A))