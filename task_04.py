def sort_list(arr):
    res = arr
    min = None
    max = None
    for elem in arr:
        if max == None or elem > max:
            max = elem
        if min == None or elem < min:
            min = elem
    for i in range(len(arr)):
        if res[i] == min:
            res[i] = max
        elif res[i] == max:
            res[i] = min
    if min != None:
        res.append(min)
    return res

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))