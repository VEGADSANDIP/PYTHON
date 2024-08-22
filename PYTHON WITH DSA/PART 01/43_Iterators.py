# set = {1,2,3,4,5,6,7,8,9,4,5,5}
# tuple = ("sandip","vegad")
# for i in tuple:
#     print(i)

list = [1,2,3,4,5,6,"sandip vegad"]
var = iter(list)
print(var) #<list_iterator object at 0x00000278907396C0>
print(var.__next__)
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
# print(next(var))
