inputs = input("Enter a numbers: ")
array = [int(x) for x in inputs.split(" ")]
k = array[0]
for _ in range(abs(k)):
    print(inputs)