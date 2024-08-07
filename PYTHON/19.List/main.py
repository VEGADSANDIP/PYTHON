#  list is one name and his under are many name
# order collection of data type
marks = [33,33,55,44,89,"sandip"]
print(marks)
print(type(marks))
print(marks[2]) #staring index are 0
print(marks[4]) #list length  are 5
print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])

if "sandip" in marks:
  print("yes")
else:
  print("no")
  
# same thing aplly on string
if "sai" in "sandip":
  print("yes")
else:
  print("no")

print(marks[0:5:2])

# lilst comprehension = at time creat list
mark = [i+i for i in range(4)]
print(mark)