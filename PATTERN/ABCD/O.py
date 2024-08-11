for row in range(6):
    for col in range(6):
        if((col in [0,5] and row not in [0,5]) or (row in [0,5] and col not in [0,5])):
            print("*",end="")
        else:
            print(end=" ")
    print()