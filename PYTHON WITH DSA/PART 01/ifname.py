import __main__
from ast import main


def fun(a,b):
    return a+b
print(fun(10,20))

if __name__ == '__main__':
    fun(10,20)
    print(__name__)
    print(__main__)
