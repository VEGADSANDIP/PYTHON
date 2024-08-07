x= 4
print(x)

def hello():
    global x
    x= 5

hello()
print(x)