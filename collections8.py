def positive_elements_indexes(lst: list) -> list:
    return [i for i, x in enumerate(lst, start=1) if x > 0]

def negative_elements_indexes_from_rside(lst: list) -> list:
    return [i for i, x in reversed(list(enumerate(lst, start=1))) if x < 0]

n = int(input())
massiv = list(map(int, input().split()))

print(*positive_elements_indexes(massiv))
print(*negative_elements_indexes_from_rside(massiv))