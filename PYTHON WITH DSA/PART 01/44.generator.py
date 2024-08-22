def function(parameter):
    a=0
    b=10
    while True:
        try:
            result = a+b
            if(result<parameter):
                print("pela")
                yield result
                print("pashi")
                a=a+10
                b=b+10
            else:
                break
        except RuntimeError:
            print("bus bhai")
obj = function(100)
# print(obj)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# print(next(obj))
