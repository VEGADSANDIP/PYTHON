# #  hamesha excute code thay

# try:
#   l = [1,2,4,5,6]
#   i = int(input("enter the index value :"))
#   print(l[i])
# except:
#   print("kuch erroe aya")

# finally:
#   print("try ave ke except par pan hu to ececuted thai sh")

# # sidha print karvi to == same function in not vailad

def func():  
  try:
    l = [1,2,4,5,6]
    i = int(input("enter the index value :"))
    print(l[i])
    sum = l[i]+l[i+1]
    print(sum)
    return l
  except:
    print("kuch erroe aya")
    return 0
  
  finally:
    print("try ave,except ave,pan executed thai sh")

x =func()
print(x)