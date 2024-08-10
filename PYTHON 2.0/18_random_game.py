import random
while True:
    R_number = random.randint(1,100)
    U_number = int(input("enter the number between 1 to 100 = "))
    print(f"random number = {R_number}")
    print(f"user number = {U_number}")
    if(R_number > U_number and U_number<=100):
        print(f"grater number is random number = {R_number} not user number = {U_number}")
    elif(R_number < U_number and U_number<=100):
        print(f"grater number is user number = {U_number} not random number = {R_number}")
    elif(R_number == U_number and U_number<=100):
        print(f"grater number is user number = {U_number} same  random number = {R_number}")
    else:
        print(f"please enter the valid number between 1 to 100 not greater than 100 your number is {U_number}")
