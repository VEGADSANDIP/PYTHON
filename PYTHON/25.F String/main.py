var =  "my name is sandip vegad. i from gujarat "
print(var)

var = "my name is {} ,i am from {}"
name = "sandip"
country ="india"
print(var.format(name,country))

var = "my name is {1},i am from {0}"
name = "sandip"
country ="india"
print(var.format(country,name))

name = "sandip"
country ="india"
print(f"my name is {name} ,i am from {country}")
print(f"my name is {{name}} ,i am from {{country}}")

print(f"{20*30}")
