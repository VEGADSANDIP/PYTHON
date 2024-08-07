class student():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self.name)
        
    def showfunction(self):
        print(f"this is {self.name} and {self.age}")
        
class program(student):
    
    def language(self):
        print(f"there are python")   
        
        
var = student("sandip",45)
var.showfunction()
var1 = program("dhaval",20)
# var1.showfunction()
var1.language()
# print(var.name)
# print(var.age)