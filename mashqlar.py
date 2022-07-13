from types import LambdaType


def into_str(a):
    return(str(a))
a = 2
# print(type(into_str(a)))
# print(into_str(a))

def juft(mylist):
    new_list = []
    for i in mylist:
        if i%2==0:
            new_list.append(i)
    return new_list
# print(juft([1, 2, 3, 4, 5, 6]))

def toq(mlist):
    the_list = []
    for i in mlist:
        if i % 2 == 1:
            the_list.append(i)
    if len(the_list) == 0:
        return "Toq son yo'q"
    else:
        return the_list
# print(toq(mlist=[2, 4, 6, 8, 10]))

def isNumber(a):
    return True if type(a) == int or type(a) == float else False

def isNumber(a):
    return type(a) == int or type(a) == float
# print(isNumber(3.9))
# print(isNumber(3.9))


ifunc = lambda a: type(a) in [int, float]

sum_list = lambda a: sum(a)

# print(sum_list([4, 3, 2, 4, 85, 7]))
# print(ifunc("Привет :) "))

from functools import lru_cache

@lru_cache
def fib(a):

    # print("fib a=", a)
    if a == 0 or a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)
# print(fib(22))

# 1 1 2 3 5 8 13 21 34 55 89 






           