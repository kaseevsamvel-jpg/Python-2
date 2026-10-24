input()
a = input().split()
input()

to_delete = {int(x) - 1 for x in input().split()}

result = [x for i, x in enumerate(a) if i not in to_delete]
print(' '.join(result))