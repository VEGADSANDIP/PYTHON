for raw in range(0,5):
    for col in range(0,5):
        if(col in [0,4] or raw in [0,4]):
            print("*",end="")
        else:
            print(end=" ")
    print()