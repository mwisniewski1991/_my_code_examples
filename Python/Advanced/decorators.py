def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('STH IS HAPPEN')
        func(*args, **kwargs)
    return wrapper


# dec = my_decorator(say_hello)
# dec()

@my_decorator
def add_one(value: float) -> float:
    return value + 1


@my_decorator
def say_hello() -> None:
    print('hello')

say_hello()
print(add_one(6))