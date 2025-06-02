import datetime
import time

cache = {}
cached_time = {}


def cached(*c_args, **c_kwargs):
    max_size = None
    seconds = None
    for key, arg in c_kwargs.items():
        if key == "max_size" and type(arg) is int:
            max_size = arg
        elif key == "seconds" and type(arg) is int:
            seconds = arg
    if type(c_args[0]) == list:
        if len(c_args) == 2:
            max_size = c_args[0][0]
            seconds = c_args[0][1]
        elif len(c_args) == 1:
            max_size = c_args[0][0]
    else:
        for i in range(len(c_args)):
            if i == 0 and type(c_args[0]) is int:
                max_size = c_args[0]
            if i == 1 and type(c_args[1]) is int:
                seconds = c_args[1]

    def decorator(func):
        def caching(*args, **kwargs):
            if not isinstance(seconds, type(None)):
                time_atm = datetime.datetime.now()
                to_del = []
                for key, c_time in cached_time.items():
                    if time_atm - c_time > datetime.timedelta(seconds=seconds):
                        to_del.append(key)
                for key in to_del:
                    del cache[key]
                    del cached_time[key]
            hash_str = ""
            for arg in args:
                hash_str += str(arg)
            for kw, value in kwargs.items():
                hash_str += kw + str(value)
            if hash_str in cache:
                return cache[hash_str]
            else:
                res = func(*args, **kwargs)
                cache[hash_str] = res
                cached_time[hash_str] = datetime.datetime.now()
                if not isinstance(max_size, type(None)):
                    if len(cache) > max_size:
                        oldest_h = "#"
                        oldest_t = datetime.datetime.now()
                        for hash, t in cached_time.items():
                            if oldest_h == "#":
                                oldest_h = hash
                                oldest_t = t
                            elif t < oldest_t:
                                oldest_h = hash
                                oldest_t = t
                        del cached_time[oldest_h]
                        del cache[oldest_h]
                return res
        return caching
    return decorator


@cached(3,10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2


print(slow_function(2))
print(slow_function(3))
print(slow_function(4))
print(slow_function(5))
print(slow_function(2))
time.sleep(15)
print(slow_function(2))
