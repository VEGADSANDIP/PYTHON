for raw in range(6):
    for col in range(5):
        if(raw in [0,1,2,3,4,5]):
            print("*",end="")
        else:
            print(end=" ")
    print("*")