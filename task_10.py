char = "abcdefghijklmnopqrstuvwxyz"


def count_words(input):
    input = str(input).lower()
    length = len(input)
    res = {}
    temp_str = ""
    for i in range(length):
        a = input[i]
        if a in char:
            temp_str += a
        elif temp_str != "":
            if temp_str in res:
                res[temp_str] += 1
            else:
                res[temp_str] = 1
            temp_str = ""
    if temp_str in res:
        res[temp_str] += 1
    else:
        res[temp_str] = 1
    return res


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
