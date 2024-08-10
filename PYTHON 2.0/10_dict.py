dict = {
    "name":"sandip",
    "age":24
}
dict.update({"surname":"vegad"})
print(dict)
print(dict["name"])
print(dict.get("name"))
print(dict.keys())
print(dict.items())
for i,j in dict.items():
    print(i,"==",j)
# for i in dict.values():
#     print(i)
# del dict["name"]
# print(dict)
# dict.pop("age")
print(dict)

l = {
    "user":{"name":"sandip","age":24}
}
print(l)