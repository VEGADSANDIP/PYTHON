# print(list(filter(lambda x:x%2==0,range(1,10))))
# print(list(map(lambda x:x%2==0,range(1,10))))


A =[1,2,3,4,5,6,7,8,9,10]
# print(list)
for i in A:
    if(i%2==0):
        print(i,end=" ")
print()
print(list(filter(lambda i:i%2==0,A)))
print(list(map(lambda i:i%2==0,A)))

