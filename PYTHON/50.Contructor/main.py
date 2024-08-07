class person():
    # name = "sandip"
    # age = 18
    # Contractor
    def __init__(self,x,y):
        print("hey")
        self.name = x
        self.age = y
        print(self.name)
        

    def fun(self):
        print(f"hey {self.name} age is {self.age}")

a = person("sandip",20)
b = person("diya",20)
# a.name = "diya"
# a.age = 20
# # print(a.name,a.age)
a.fun()
# b.fun() 
