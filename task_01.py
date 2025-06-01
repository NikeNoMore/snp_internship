char = "abcdefghijklmnopqrstuvwxyz0123456789"


def is_palindrome(input):
    temp_str = str(input).lower()
    length = len(temp_str)
    i = 0
    j = length - 1
    while i <= j:
        while temp_str[i] not in char or temp_str[j] not in char:
            if temp_str[i] not in char:
                i += 1
            if temp_str[j] not in char:
                j -= 1
        if temp_str[i] != temp_str[j]:
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))