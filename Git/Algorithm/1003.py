arr = [1, 2, 3, 4, 5, 6]

res = []
for i in range(1 << len(arr)):
    sub = []
    for j in range(len(arr)):
        if i & (1 << j):
            sub.append(arr[j])
    res.append(sub)

sub = [[]]
for i in arr:
    size = len(sub)
    for j in range(size):
        sub.append(sub[j] + [i])

def perm(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in perm(arr[:i]+arr[i+1:], n-1):
            res.append([num] + j)
    return res

def combi(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in combi(arr[i+1:], n-1):
            res.append([num] + j)
    return res

print(perm(arr, 3))
print(combi(arr, 3))