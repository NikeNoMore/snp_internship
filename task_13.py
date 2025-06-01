import datetime
import time

cache = {}
cached_time = {}


def cached(max_size=None, seconds=None):
    def decorator(func):
        def caching(*args, **kwargs):
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
            elif len(cache) < max_size or not max_size:
                res = func(*args, **kwargs)
                cache[hash_str] = res
                cached_time[hash_str] = datetime.datetime.now()
                return res
        return caching
    return decorator


@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2


print(slow_function(2))
print(slow_function(2))
time.sleep(15)
print(slow_function(2))
