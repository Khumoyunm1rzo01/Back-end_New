def mydecorator(func):
    def inside(*args, **kwargs):
        print("Salom dasturchilar")
        a = func(**args, **kwargs)
        print("Salom dasturchilar")
        return a
    return inside
@mydecorator
def max(a, b):
    return a if a > b else b

@mydecorator
def salom():
    print("salom")
    
salom()
# print(max(1, 2))