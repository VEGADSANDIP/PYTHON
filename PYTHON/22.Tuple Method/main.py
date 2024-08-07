# name = ("sandip","aryan","dhaval","sumit","mnisha")
# print(name)

# new_tuple = list(name)
# print(new_tuple)
# new_tuple.append("ranekina")
# print(new_tuple)
# new_tuple.pop(3)
# print(new_tuple)
# name = tuple(new_tuple)
# print(name)

# there are two tuple cobine in another tuple
number = (0,1,2,3,5,0,1,3,1,4,5,2,3,1)
print(number)

print(number.count(1)) #that is similer to print
var = number.count(1)
print(var)

# index method 
# var.tuplename(element,stat,end)
print(number.index(1))
print(number.index(1,4,12))