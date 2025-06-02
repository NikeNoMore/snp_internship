import datetime


def date_in_future(*args):
    res = datetime.datetime.now()
    if len(args) == 1:
        if type(args[0]) == int:
            added_days = datetime.timedelta(days = args[0])
            res += added_days
    return res


print(date_in_future())
print(date_in_future(2))
