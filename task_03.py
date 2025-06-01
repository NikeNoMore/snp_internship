def max_odd(arr):
    res = None
    for elem in arr:
        if type(elem) is int or type(elem) is float:
            if elem % 3 == 0 and (res == None or elem > res):
                res = elem
    return res

print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))