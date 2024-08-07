var = int(input("enter the any one of number in 1.snake 2.water 3.gun  \"player 1\"  == "))
var1 = int(input("enter the any one of number in 1.snake 2.water 3.gun  \"player 2\" == "))

if(var == var1): #similar
    print("game is drove")
elif(var == 1 and var1 == 2 or var == 2 and var1 == 1): # snake > water 
    print("snake is winner")
elif(var == 1 and var1 == 3 or var == 3 and var1 == 1): # snake < gun
    print("gun is winner")    
elif(var == 2 and var1 == 3 or var == 3 and var1 == 2): # water > gun
    print("gun is winner")
else:
    print("please enter the valid details")


