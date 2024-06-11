import gc

class Test:
    pass
test = Test()

print(test in gc.get_objects(generation=0))
gc.collect(generation=0) #manual start garbage colletor
print(test in gc.get_objects(generation=0))
print(test in gc.get_objects(generation=1))
