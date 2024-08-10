class A:
    def AsdOne(self):
        print("One");
class B():
    def AsdTwo(self):
        print("two");         
class C(A,B):
    def AsdThree(self):
        print("Three");         
obj = C();
# obj.AsdOne()
# obj.AsdTwo()
obj.AsdThree()
