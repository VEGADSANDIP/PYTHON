import functools
num = [1,2,3,4,5,6,7,8,9,10]
print(functools.reduce(lambda x,y:x+y,num))


print(list(map(lambda x:x*x*x, range(1, 11))))

print(list(filter(lambda x:(x % 2 != 0) and (x % 3 != 0), range(2, 25))))


