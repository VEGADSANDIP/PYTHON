s1 = {1,2,3,5,6}
s2 = {3,6,7}
#union set there are commmined
print(s1,s2)
print(s1.union(s2)) 

# update s1 then result
s1.update(s2)
print(s1)

# inter section 

s1 = {"bhavnagar","gita mandir","modasa","rajkot"}
s2 = {"bhavnagar","khodiyar mandir","modasa","dwarka","rajkot"}
# s2 = {"modasa","rajkot"}
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s2.difference(s1))
#true or false == same value haseh to answer flase
print(s1.isdisjoint(s2))
# s2 ni badhi value s1 ma hoy to true
print(s1.issuperset(s2))
s1.add("hello") 
print(s1)

s1 = {"bhavnagar","gita mandir","modasa","rajkot"}
# s1.remove("koltal") #show error
# print(s1)

s1.discard("koltal")
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)





