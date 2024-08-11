for row in range(6):
    for col in range(5):
        if((col in [0,4]  and row not in [0,4,5]) or (row in [0,4] and col not in [0,4]) or (row in [5] and col not in [0,1,2,3]) or (row in [3] and col not in [1,3])  ):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
    
    
