class BaseClass:
    def Name(self):
        print("sandip")

class NewClass(BaseClass):
    def Surname(self):
        print("Vegad")

class NewClass1(BaseClass,NewClass):
    def FatherName(self):
        print("Hareshbhai")

a = NewClass1()
a.Name()
a.Surname()
a.FatherName()
