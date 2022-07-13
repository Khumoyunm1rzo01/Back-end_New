# def func():
#     son = int(input("Sonni kiriting: "))
#     print(son**3)
# func()

# def daraja_3(a):
#     return a**3
# natija = int(input("Sonni kiriting: "))
# print(daraja_3(natija))

# def daraja_n(s,a):
#     return s**a
# san = int(input("Sonni kiriting: "))
# san2 = int(input("Sonni kiriting: "))
# javob = daraja_n(san, san2)
# print(javob)

# def join_names(ism1:str, ism2, ism3):
#     ism1 = ism1.capitalize() # katta qilib qo'yadi bosh harifini
#     ism2 = ism2.capitalize()
#     ism3 = ism3.capitalize()
#     s = ism1 +" "+ism2+" "+ism3
#     return s
# print(join_names("ali", "Guli", "VAli"))

def join_words(word1, word2, word3, belgi):
    word1 = word1.upper()
    word2 = word2.upper()
    word3 = word3.upper()
    s = word1 + belgi + word2 + belgi + word3
    return s
print(join_words("python", "dasturlash", "tili"))



