def sequence_generator(a, n):
    value = a
    yield value
    for i in range(2, n + 1):
        value = value * (i - 10) + a
        yield value

a = int(input())
indices = list(map(int, input().split()))
array = list(sequence_generator(a, max(indices)))
result = sum(array[i - 1] for i in indices)
print(result)
