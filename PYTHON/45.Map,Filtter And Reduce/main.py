# # MAp
def cube(x):
    return x*x*x

print(cube(5))

l = [1,2,3,4,5]
var = []
for item in l:
    var.append(cube(item))

var = list(map(cube,l))
print((var))
print(type(var))   

# #Filter 

def filter_function_name(a):
    return a>3

var = list(filter(filter_function_name,l))  # type: ignore
print(var)


# reduce

from functools import reduce

number = [1,2,3,4,5,6]

def mysum(x,y):
    return x + y

sum  = reduce(mysum,number)

print(sum)