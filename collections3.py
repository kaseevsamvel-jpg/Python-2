inputs1 = input("Enter a numbers: ")
array1 = [int(x) for x in inputs1.split(" ")]

inputs2 = input("Enter a numbers: ")
array2 = [int(x) for x in inputs2.split(" ")]

result = [array1, array2]
result = sorted(result, key=len)
for i in result:
    print(" ".join(str(x) for x in i))