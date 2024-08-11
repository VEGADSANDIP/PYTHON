for row in range(6):
    for col in range(6):
        if((col == 0 or col == 5) or (col == 1 and row not in [0,2,3,4,5,6]) or (col == 2 and row not in [0,1,3,4,5,6]) or (col == 3 and row not in [0,2,1,4,5,6]) or (col == 4 and row not in [0,2,3,1,5,6])):
            print("*",end="")
        else:
            print(end=" ")
    print()