string = "animal base cat"
dict = {"a":"@","b":"2","c":"3"}
str1 = "abc"
str2 = "@23"
table = string.maketrans(dict)
# table = string.maketrans(str1,str2)
print(table) #table
print(string.translate(table))
# print(ord("s"))