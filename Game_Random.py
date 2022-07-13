from operator import itemgetter
from random import randint
tasodifiy_son = randint(1, 100)
urinishlar = 1


while True:
    son = int(input("Shunday ikki  honali sonni kiritingki u kompyuter o'ylagan son bo'lib chiqsin: "))
    if son > tasodifiy_son:
        print(son, "dan kichik")
    elif son < tasodifiy_son:
        print(son, "dan katta")
    else: 
        break
    urinishlar += 1

print("Tabriklaymiz siz kompyuter o'ylagan sonni topdingiz :)")
print("Kompyuter o'ylagan son: ", tasodifiy_son)
print("Siz", urinishlar, "marotaba urinishda kompyuter o'ylagan sonni topdingiz!")
input()
