import sys

var1 = [1,2,3]
var2 = 'x'

print(hex(id(var1)))
print(hex(id(var2)))


var_1 = 1
var_2 = 2
var_3 = 3
var_4 = 4
var_5 = 5
var_6 = 6
var_7 = 7
var_8 = 8
var_9 = 9
var_10 = 10
var_33 = 33


print(sys.getrefcount(var_1))
print(sys.getrefcount(var_2))
print(sys.getrefcount(var_3))
print(sys.getrefcount(var_4))
print(sys.getrefcount(var_5))
print(sys.getrefcount(var_6))
print(sys.getrefcount(var_7))
print(sys.getrefcount(var_8))
print(sys.getrefcount(var_9))
print(sys.getrefcount(var_33))