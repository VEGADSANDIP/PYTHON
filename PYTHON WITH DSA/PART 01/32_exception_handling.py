import math
while True:
    number = int(input("enter the number "))
    try:
        if number<0:
            raise ValueError("do not accept the negative number ",number)
        result = math.factorial(number) # type: ignore
        print(result)
    except ValueError as e:
        print(e)
    finally:
        print("my name is sandip vegad")

