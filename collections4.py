list_A = [int(x) for x in input().split()]
f, k = [int(x) for x in input().split()]

if f <= k <= (f + len(list_A) - 1): 
    print(list_A[k - f])
else:
    print("Error")