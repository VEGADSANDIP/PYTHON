tuple = (10,20,30,40,50,60,70)
print(type(tuple),tuple)

for i in tuple:
    print(i,tuple)
       
print(max(tuple))
print(min(tuple))
a = tuple.count(20)
print(a)
print(tuple.index(20))

a =sum(tuple)
print(a)