class dog:
    def sound(self):
        print("ohh")

class cat:
    def sound(self):
        print("miyav")

def AllSound(e):
    e.sound()

obj1 = dog()
obj2 = cat()
AllSound(obj1)
AllSound(obj2)