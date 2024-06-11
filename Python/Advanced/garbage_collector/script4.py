import gc

class Test:
    def __del__(self):
        print("Removing object")

print(f'{gc.get_count()=} before collect')
gc.collect() #manual start garbage colletor
print(f'{gc.get_count()=} after collect')

test = Test()
test.tt = test

print(f'{gc.get_count()=} after creating object')
del test
print(f'{gc.get_count()=} afetr removing object')

gc.collect() #manual start garbage colletor

print(f'{gc.get_count()=} after second collect')
