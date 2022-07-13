from datetime import datetime
vaqt = datetime.now()
if  vaqt.weekday() == 0:
    print("Bugun hafta kunining Dushanba kuni.")
elif vaqt.weekday() == 1:
    print("Bugun hafta kunining Seshanba kuni.")
elif vaqt.weekday() == 2:
    print("Bugun hafta kunining Chorshanba kuni.")
elif vaqt.weekday() == 3:
    print("Bugun hafta kunining Payshanba kuni.")
elif vaqt.weekday() == 4:
    print("Bugun hafta kunining Juma kuni.")
elif vaqt.weekday() == 5:
    print("Bugun hafta kunining Shanba kuni.")
elif vaqt.weekday() == 6:
    print("Bugun hafta kunining Yakshanba kuni.")
else:
    print("Bunday kun mavjud emas!")



# import time 
# t1 = time.time()

# time.sllep(2)

# t2 = time.time()
# print("Ketgan vaqt", t2-t1)