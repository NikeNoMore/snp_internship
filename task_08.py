nums = '0123456789'


def multiply_numbers(input = []):
    input = str(input)
    res = None
    for elem in input:
        if type(elem) is int or elem in nums:
            if not res:
                res = int(elem)
            else:
                res *= int(elem)
    return res


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))