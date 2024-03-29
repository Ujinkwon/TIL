arr = [1, 2, 3, 4, 5, 6, 7]

res = [[]]
for i in arr:
    size = len(res)
    for j in range(size):
        res.append(res[j] + [i])
    
def perm(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in perm(arr[:i]+arr[i+1:], n-1):
            res.append([num]+j)
    return res

def combi(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in combi(arr[i+1:], n-1):
            res.append([num]+j)
    return res
print(combi(arr, 2))