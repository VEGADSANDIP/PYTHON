for row in range(7):
    for col in range(5):

        var = row not in range(1,6)
        var1 = row not in [0,2,3,4,6]
        var2 = row not in [0,1,3,5,6]

        if(col == 0 or (col == 4 and (var)) or (col == 3 and (var1)) or (col == 2 and (var2))):
            print("*",end="")
        else:
            print(end=" ")
    print()