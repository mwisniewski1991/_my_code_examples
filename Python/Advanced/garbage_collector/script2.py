import sys

var1 = object()
print(sys.getrefcount(var1)) #2

a = []
a.append(a)
print(sys.getrefcount(a)) #3
del a