for row in range(7):
    for col in range(5):
        if((col in [0] and row not in []) or (row in [0,3] and col not in [0,4]) or (col in [4] and row not in [0,3,4,5,6])):
            print("*",end="")
        else:
            print(end=" ")
    print()