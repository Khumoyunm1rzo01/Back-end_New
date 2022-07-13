# def qoshuv(sonlar):
#     summa = 0
#     for i in str(sonlar):
#          summa += int(i)
#     print(f'Yigindi soni {summa} uzunligi {len(str(sonlar))}')

# qoshuv(555)

# def Y(a, b):
#     if a+b>100:
#         print(a+b)
#     else:
#         if a>b:
#             print(a-b)
#         else:
#             print(b-a)
# Y(50, 50)

a = int(input("Sonni kiriting: "))
b = int(input("Sonni kiriting: "))
raqamlar = range(a, b)
for raqam in raqamlar:
     print(f"{raqam} ning kvadrati {raqam**2} ga teng")
