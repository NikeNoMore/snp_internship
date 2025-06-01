def connect_dicts(dict1, dict2):
    res = {}
    to_check = {}
    sum_dict1 = 0
    sum_dict2 = 0
    for (key, value) in dict2.items():
        if value >= 10:
            res[key] = value
        sum_dict2 += value
    for (key, value) in dict1.items():
        if value >= 10:
            if key in res:
                to_check[key] = value
            else:
                res[key] = value
        sum_dict1 += value
    if sum_dict1 > sum_dict2:
        for (key, value) in to_check.items():
            res[key] = value
    res = dict(sorted(res.items(), key=lambda item: item[1]))
    return res


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
