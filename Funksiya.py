# def func():
#     print("Salom bu -func- funksiyasi")
#     a = 5
#     b = 9
#     print(a*b)
# func()


# def perimetr(a, b):
#     p = 2 * (a+b)
#     print(p)

# perimetr(3,8)
# perimetr(b=5, a=1)
# perimetr(6, b=9)


# -ABS- Finksiya
# def modul(son):
#     if son < 0:
#         return son * -1
#     else:
#         return son

# son = modul(-2)
# print(modul(-2))
# print(modul(-2))


def yigindi(sonlar):
    summa = 0
    for i in sonlar:
        summa += i
    return summa

print(sum([1, 2, 3]))
# print(yigindi([1, 2, 3]))

# sonlarni katta kichikligini topish
# def kattasi(*sonlar):
#     k = sonlar[0]
#     for i in sonlar:
#         if k < i:
#             k = i
#     return k

# print(kattasi(3, 7))
# print(kattasi(3, 7, 7, 9))


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs.get("ism","Ism parametri jo'natilindi"))

# func(2, 1, 5, ism="Humoyunmirzo", kasb="Dasturchi")


# def chop_qil(*args, sep="", end="\n"):
#     print(*args, sep=sep, end=end)

# def kitir(matn):
#     return input(matn)

# chop_qil("Salom", "qalesan?", sep="-")
# a = kitir("Sonni kiriting: ")
# chop_qil(a)