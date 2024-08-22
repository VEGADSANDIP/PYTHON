class person:
    __name=""
    def __init__(self):
        self.__name = "sandip"
    def Surname(self):
        print("vegad")
        print(self.__name)
    # def Name(self,name):
    #     self.__name = name
    #     print(self.__name)

obj = person()
obj.Surname()
# obj.Name("hareshbhai")
obj.__name = "swami"
obj.Surname()
