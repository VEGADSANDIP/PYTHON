list = [];

while True:
    print("select the value")
    user = int(input("""
                     1.push
                     2.pop
                     3.peek
                     4.display
                     5.exist
                     """))
    if(user == 1):
        a = int(input("enter the value"))
        list.append(a)
        print(list)
    elif(user == 2):
        if(len(list)==0):
            print("khali she")
        else:
            b = list.pop()
            print(b)
            print(list)
    elif(user == 3):
        if(len(list)==0):
            print("khali she")
        else:
            print("last element == ",list[-1])
            print(list)        
    elif(user == 4):
        print("list = ",list)
    else:
        print("bye..")
        break
        
    
    
            