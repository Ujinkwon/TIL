import copy

# 부분집합
arr = [1, 2, 3]
# 1. 단순 반복문과 배열
subsets = [[]]
for i in arr:
    size = len(subsets)
    for j in range(size):
        subsets.append(subsets[j] + [i])
print(subsets)

# 2. 재귀
# def recur(subset, i, arr):
#     if i == len(arr):
#         res.append(copy.copy(subset))
#         return
#     else:
#         subset.append(arr[i])
#         i += 1
#         recur(subset, i, arr)
#         subset.pop()
#         recur(subset, i, arr)
# res = []
# recur([], 0, arr)
# print(res)

# 3. 비트연산
# res = []
# for i in range(1 << len(arr)):
#     subset = []
#     for j in range(len(arr)):
#         if i & (1<<j):
#             subset.append(arr[j])
#     res.append(subset)
# print(res)


arr = [1, 2, 3, 4]
n, m = 4, 3
# 순열
# n개 중 m개 뽑기 / 중복 x / 순서 o
# def perm(n, m, level):
#     if level == m:
#         print(res)
#         return
#     for i in range(n):
#         if not check[i]:
#             check[i] = 1
#             res[level] = arr[i]
#             perm(n, m, level+1)
#             check[i] = 0    # 48줄, 51줄 없으면 중복 순열
# res = [0]*m
# check = [0]*n
# perm(n, m, 0)
# print()

arr = [0, 1, 2, 3]

def perm(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in perm(arr[:i] + arr[i+1:], n-1):
            res.append([num] + j)
    return res
print(perm(arr, 2))

def perm2(arr, n):
    res = []
    if n > len(arr):
        return res
    if n == 1:
        for i in arr:
            res.append([i])
    elif n > 1:
        for i in range(len(arr)):
            temp = [i for i in arr]
            temp.remove(arr[i])
            for j in perm2(temp, n-1):
                res.append([arr[i]] + j)
    return res
print(perm2(arr, 2))

# 조합
# n개 중 m개 뽑기 / 중복 x / 순서 x
# def combi(n, m, level, idx):
#     if level == m:
#         print(res)
#         return
#     for i in range(idx, n):
#         res[level] = arr[i]
#         combi(n, m, level+1, i+1)   # i+1 말고, i면 중복 조합
# res = [0]*m
# combi(n, m, 0, 0)

def combi(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        num = arr[i]
        for j in combi(arr[i+1:], n-1):
            res.append([num] + j)
    return res
print(combi(arr, 2))

def combi2(arr, n):
    res = []
    if n > len(arr):
        return res
    if n == 1:
        for i in arr:
            res.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1):
            for j in combi2(arr[i+1:], n-1):
                res.append([arr[i]]+j)
    return res
print(combi2(arr, 2))

