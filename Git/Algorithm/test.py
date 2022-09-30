arr = [3, 6, 7, 1, 5, 4]

for i in range(1 << len(arr)):
    for j in range(len(arr)):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()

res = [[]]
for i in arr:
    size = len(res)
    for j in range(size):
        res.append(res[j] + [i])
print(res)

def perm(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in perm(arr[:i]+arr[i+1:], n-1):
            res.append([num] + j)
    return res
print(perm(arr, 3))

def combi(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in combi(arr[i+1:], n-1):
            res.append([num] + j)
    return res
print(combi(arr, 3))