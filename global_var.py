x = "awesome global var"

def myfunc():
    #global x
    x = "fantastic global var"
    print(x)

myfunc()

print(x)
