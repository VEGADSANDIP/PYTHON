# public
class student():
    def __init__(self,x,y):
        print("hey")
        self.name = x
        self.age = y
        
    def staff(self):
        print(f"hey {self.name} your age is {self.age}")
        
a = student("sandip",20)
a.staff()
# private
# protected 