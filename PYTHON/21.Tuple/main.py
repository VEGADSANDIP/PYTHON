#smallest tuple is (1,)
tup = (1,56,48,96,23,510,56)
print(tup,"\n",type(tup),"\n",tup[0],"\n",tup[1:5])

if 56 in tup:
  print("yes")
else:
  print("no")

tup2 = tup[1:5]
print(tup2)