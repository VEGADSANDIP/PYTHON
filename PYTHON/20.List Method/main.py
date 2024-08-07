l = [11,54,6,8,9,4,5,5]
# print(l)
# print(type(l))
# print(l[1])

# method
# add the list
l.append(20)
print("add the data",l)
# increment or dicrement
l.sort()
print("sort the data",l)

l.reverse()
print("reverse the data",l)

print("serch inex value = ",l.index(20))
print("count the numberr of value = ",l.count(5))

l.insert(1,899) #frist is index and second is data
print("insrt the data ",l)

m = [50,56,58]
k = l+m
print("merge data",k)
