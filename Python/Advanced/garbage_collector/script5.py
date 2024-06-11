import gc
from time import sleep

print(f'{gc.get_threshold()=}')
gc.set_threshold(400, 5, 5)
print(f'{gc.get_threshold()=}')

# class A:
#     def __init__(self):
#         self.vars = list(range(100_000))

# gc.callbacks.append(lambda x,y: print(x,y))

# for _ in range(1000):
#     a = A()
#     a.self_ref = A
#     sleep(0.00001)
