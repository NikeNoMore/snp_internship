import datetime


def date_in_future(*args):
    res = datetime.datetime.now()
    if len(args) == 1:
        if type(args[0]) == int:
            added_days = datetime.timedelta(days = args[0])
            res += added_days
    result = [str(res.day), str(res.month), str(res.year), str(res.hour), str(res.minute), str(res.second)]
    for i in range(len(result)):
        if i != 2:
            if len(result[i]) < 2:
                result[i] = "0" + result[i]
    return "{0}-{1}-{2} {3}:{4}:{5}".format(result[0], result[1], result[2], result[3], result[4], result[5])


print(date_in_future())
print(date_in_future(2))
