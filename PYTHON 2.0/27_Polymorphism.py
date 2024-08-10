class User:
    def Name(self):
        print("welcome to")

class Person(User):
    def Age(self,):
        super().Name()
        print("sandip vegad")

obj = Person()
obj.Age()