def coincidence(arr = [], arr_range = range(0)):
    a = arr_range.start
    b = arr_range.stop
    res = []
    for num in arr:
        if type(num) is int or type(num) is float:
            if b > num >= a:
                res.append(num)
    return res


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))