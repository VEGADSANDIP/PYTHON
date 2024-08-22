
# list = [10,54,6,2,32,56,21,25,59,98]
# list.sort()
# print(list)

# list = ["aa","ccc","ddd","eededd","bbb","bba"]
# print(sorted(list))

# list = [[2,9],[1,8],[0,5]]
# # list.sort()
# # print(list)
# def sort(element):
#     return element[1]
# list.sort(key=sort)
# print(list)

# list = [124,5,8,89,5,56,4,12,4466,45]
# var =sorted(list)
# print(var)

# tuple = ((11,2,2),(2,2,5),(4,5,5),(8,93,5))
# var = sorted(tuple)
# print(var)

d = {3:"c",2:"b",1:"a"}
var = sorted(d.items())
print(var)

d={3:"a",2:"c",1:"b"}
var = sorted(d.items(),key=lambda x:x[1])
print(var)


set = {1,1,1,5,5,6,98,8,8,8}
var =sorted(set)
print(var)
