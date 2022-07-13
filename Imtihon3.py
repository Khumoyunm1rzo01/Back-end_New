# mylist = ["9", "35", "18"]
# kichik = mylist[0]
# katta = mylist[0]
# ortayosh = mylist[0]
# soni = 0
# soni1 = 0
# soni2 = 0
# for i in mylist:
#     if i < kichik:
#         kichik = i
#         soni = 1
#     elif i == kichik:
#         soni += 1
# print(kichik, "Eng kichik yosh,", soni, "ta bor")
# for i in mylist:
#     if i > katta:
#         katta = i
#         soni1 = 1
#     elif i == katta:
#         soni1 += 1
# print(katta, "Eng katta yosh,", soni1, "ta bor")
# summa = 0
# for i in mylist:
#     summa += i
# orta = summa//len(mylist)
# print(orta)

ages = [23, 17, 16, 18, 20, 22]
print("Kichik yosh =", min(ages))
print("Katta yosh =", max(ages))
print("O'rtacha yosh =", round(sum(ages)/len(ages),2))









