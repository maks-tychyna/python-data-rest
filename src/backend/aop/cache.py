from collections import OrderedDict
from functools import wraps
from threading import RLock


class Cache(OrderedDict):
    def __init__(self, maxsize: int = 128, *args, **kwargs):
        self.maxsize = maxsize

        if not self.maxsize:
            raise TypeError('Expected maxsize to be an integer and must gt 0')

        super(Cache, self).__init__(*args, **kwargs)

    def add(self, key, value):
        if key not in self and self.maxsize <= len(self):
            self.popitem(last=False)

        self[key] = value


def cached(maxsize: int, make_key=lambda args, kwargs: str(args[0])):
    def cache_wrapper(func):
        lock = RLock()
        cache = Cache(maxsize)

        @wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                key = make_key(args, kwargs)
                value = cache.get(key)
                if value is None:
                    value = func(*args, **kwargs)
                    cache.add(key, value)
                return value

        return wrapper

    return cache_wrapper


@cached(maxsize=128)
def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(20))
