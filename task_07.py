def combine_anagrams(arr):
    res = []
    for i in range(len(arr)):
        new_flag = True
        for anagram in res:
            add_flag = True
            for char in arr[i]:
                if char not in anagram[0]:
                    add_flag = False
            if add_flag:
                anagram.append(arr[i])
                new_flag = False
        if new_flag:
            res.append([arr[i]])
    return res


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))