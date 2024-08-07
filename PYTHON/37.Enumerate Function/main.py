marks = [20,35,96,25,63,48,45]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("badiya good !fail thayu ")
#   index+=1


for index,mark in enumerate(marks):
  print(index,mark,marks)
  if(index == 3):
    print("==badiya good !fail thayu ")

print("  ")

for index,mark in enumerate(marks,start=1):
  print(index,mark,marks)
  if(index == 3):
    print("==badiya good !fail thayu ")
  
    