def average(a=6,b=5):
  sum = a+b
  print(sum)

# default argument
average(4,5)
average(10)
average(b=50)

# keyword argument
average(b=10,a=5) #do not meter order

# Required argument
average(a=11) # a ni value devi padehshe

# variable length argument
def average1(*number):
  sum = 0
  for i in number:
    sum = sum + i
    print(sum)
    

c = average1(4,5)
print(c)

# return function are not completed