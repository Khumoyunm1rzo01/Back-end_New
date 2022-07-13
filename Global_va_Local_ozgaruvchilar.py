a = 9

def myfunc():
    a = 1
    def myfunc2():
        nonlocal a
        a = 8
        print(a)
    print(a)
    myfunc2()
    print(a)

print(a)
myfunc()
print(a)