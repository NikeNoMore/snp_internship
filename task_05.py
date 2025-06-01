import datetime


def date_in_future(input = 0):
    res = datetime.datetime.now()
    added_days = datetime.timedelta(days = input)
    res += added_days
    return res


print(date_in_future())
print(date_in_future(2))
