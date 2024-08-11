for row in range(7):
    for col in range(5):
        if((col == 0 or col == 4) or ((col == 1 or col == 3) and row not in [0,2,3,4,5,6]) or (col == 2 and row not in [0,1,3,4,5,6])  ):
            print("*",end="")
        else:
            print(end=" ")
    print()    