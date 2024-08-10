class Name():
    def __init__(self) -> None:
        self.__name = ""
    def GetValue(self):
        return self.__name
    def SetValue(self,Value):
        self.__name = Value
        
Asd = Name()
Asd.SetValue("dhaval")
Sdf = Asd.GetValue()
print(Sdf)