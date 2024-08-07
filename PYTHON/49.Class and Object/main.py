class person:
    name = "sandip"
    work = "std"
    networth = 10
    def fun(self): # self === "var" game telta use kari shako na ,,, var 1 call thashe in self
        print(f"{self.name} is a working by student")


var = person()
var.name = "dhaval"
var.work = "ca"
var.networth = 20
var1 = person()
var1.name = "manisha"
var1.work = "bca"
var1.networth = 200
# print(var.name,var.work,var.networth)
print(var1.name,var1.work,var1.networth)
var.fun()
var1.fun()