a = "sandip vegad 123"
l = len(a)
print(type(a),a)
print(a[0:6])
print(a[-1::-1])

for i in a:
    print(i)

print(a.lower()) 
print(a.upper()) 
print(a.title()) 
print(a.capitalize())
print(a.find("d",0)) 
print(a.index("v"))
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(ord("s"))
print(chr(65))
a = 1
b = 2
print(f"sandip {a} and vegad {b}")


    