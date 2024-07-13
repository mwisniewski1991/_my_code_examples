from time import perf_counter, sleep 
from functools import wraps

def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''wrapper doc'''
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        print(f'{func.__name__}() took {end_time - start_time:.3f}s')
    return wrapper

@get_time
def add_one(value: float) -> float:
    '''add_one doc'''
    print(value + 1)
    sleep(2)
    return value + 1

# add_one(2)
print(add_one.__name__)
print(add_one.__doc__)