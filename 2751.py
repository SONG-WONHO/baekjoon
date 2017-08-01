def merge_sort(a):
    if len(a) <= 1: return a

    half = len(a) // 2
    L = merge_sort(a[:half])
    R = merge_sort(a[half:])
    mer = []

    while len(L) > 0 and len(R) > 0:
        if L[0] > R[0]:
            mer.append(R[0])
            R.pop(0)

        else:
            mer.append(L[0])
            L.pop(0)

    if len(L) > 0: mer += L
    if len(R) > 0: mer += R

    return mer

num_case = int(input())

num_list = []

for _ in range(num_case):
    num = int(input())
    num_list.append(num)

result = merge_sort(num_list)

for i in result:
    print(i)