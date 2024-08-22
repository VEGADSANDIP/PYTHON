# list = [78,56,2,45,9,23,20,88,0]
# print(list,"\n")

# for i in range(len(list)):
#     # print("i index = ",i)
#     min_value = min(list[i:])
#     # print("min value  = ",min_value)
#     min_ind = list.index(min_value)
#     # print("swapping index = ",min_ind)
#     list[i],list[min_ind] = list[min_ind],list[i] 

# print(list,"\n")



list = []
number = int(input("enter the element of number = "))
for i in range(number):
    element = int(input("enter the number of list = "))
    list.append(element)
# list = [50,1,45,2,63,2,0]
print(list)
for i in range(len(list)):
    min_value = min(list[i:])
    min_ind = list.index(min_value,i)
    # print(min_value,min_ind,i)
    list[i],list[min_ind] = list[min_ind],list[i]
    # print(list)
list.reverse()
print(list)

