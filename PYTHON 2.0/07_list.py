list = [10,20,30,40,50,60,70]
l =len(list)
list1 = [45,45,78]
a = list.pop(1)
# print(a)
list.append(20)
list.sort()
list.reverse()
# list.extend(list1)
list.insert(1,45)
d = list.count(10)
print(d)
print(max(list))
print(min(list))
print(list,type(list))

for a,b in zip(list,list1):
    print(a,b)
for h in range(l):
    print(list[h])    
    

# for i in list:
#     print(i)
    
# l = []
# for i in range(1,100):
#     print(i)
#     l.append(i)
# print(l)

# n = [m for m in range(1,10)]
# print(n)
