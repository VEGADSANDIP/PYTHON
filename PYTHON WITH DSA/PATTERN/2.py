while True:
    number = int(input("enter the number of line"))
    k= 1
    for i in range(1,number+1):
        for j in range(1,k+1):
            print("*",end=" ")
        k=k+2    
        print(" ")