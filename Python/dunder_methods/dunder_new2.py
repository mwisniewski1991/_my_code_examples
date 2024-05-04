# __init__ does NOT WORK 
class UppercaseTuple(tuple):
    def __init__(self, iterable):
        for i, arg in enumerate(iterable):
            self[i] = arg.upper()

class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)


print(tuple(['hi', 'hey', 'hello']))
print(UppercaseTuple(['hi', 'hey', 'hello']))