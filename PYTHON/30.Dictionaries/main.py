from collections.abc import KeysView


var =  {'name':'sandip','age':'20','eligible':'true'}
print(type(var))

print(var["name"])

print(var.get("name")) #none item are result
print(var.keys()) # only name age 
print(var.values()) # sandip 20 
print(var.items()) # both in ()

for i in var:
  # print(i)
  print(var[i])

for key,value in var.items():
  print(f"the {key} is {var[key]}")