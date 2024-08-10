# class A:
#     def Name(self):
#         print("sandip vegad")
# class B(A):
#     def Name(self):
#         # super().Name()
#         print("Dhaval vegad")
        
# obj = B()
# obj.Name()


class Math:
    def Sum(self,a = None,b = None):
        # print(a+b)
        if(a!=None and b!=None):
            print(a+b)
        elif(a!=None):
            print("a is",a)
        else:
            print("false")

obj = Math()
obj.Sum(90,50)