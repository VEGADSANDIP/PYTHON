# hello pela good morning kare pashi 
# modified to function


    
def greet(fx):
    def mfx(*args,**kwargs):  # arg is argument mate she ----- args ==tuple  and kwargs == dict
        print("good morning ")
        fx(*args,**kwargs)
        print("thnks")
    return mfx
@greet #modified function ==== pela ane pashi kai kam thay she
def hello():
    print("hello")
    
@greet
def sum(a,b):
    sum = a+b
    print(sum)

hello()
sum(4,5)

    
    