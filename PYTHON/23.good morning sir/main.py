import time
var = time.strftime('%H:%M:%S')
print(var)
hour = int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
  print("good morning ala")
elif(hour>=12 and hour<18):
  print("good morning ala")
elif(hour>=18 and hour<0):
  print("good morning ala")