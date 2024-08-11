# for raw in range(0,5):
#     for col in range(0,3):
#         if(((raw in [0,1,2]) and col not in [1,2]) or (raw in [1,2] and col not in [2]) or (raw in [2]) ):
#             print("*",end="")
#         else:
#             print(end="")
#     print()
    
for row in range(5):
    for col in range(3):
        if (row in [0, 1, 2] and col == 0) or (row == 2):
            print("*", end="")
    print()
