class Bike:
    def __init__(self,stoke):
        self.stoke = stoke
    def DisplayBike(self):
        print("total number of bike  = ",self.stoke)
    def BuyBike(self,number):
        if(number<=0):
            print("positive number ")
        elif(number>self.stoke):
            print("not available")
        else:
            print("total price your bike ",number*100);
            print("available bike ",(self.stoke - number))
        
while True:
    obj = Bike(100)
    uc = int(input('''1.display 2.rent bike 3.exist  
enter the number == '''))
    if(uc == 1):
        obj.DisplayBike()
    elif(uc == 2):
        n = int(input("enter the bike number "))
        obj.BuyBike(n)