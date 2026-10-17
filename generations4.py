input()
n = int(input())
all_balls = [int(x) for x in input().split()]
balls = [m for m in all_balls if 3 < m < 20]
my_sum = sum(balls)
print(my_sum)

