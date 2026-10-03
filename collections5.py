def sequence_generator(a):
    value = a
    while True: 
        yield value

        value = (value * value) % 100 - 5 * value + 6

a = int(input())
gen = sequence_generator(a)
result = [next(gen) for _ in range(10)]
print(*result)