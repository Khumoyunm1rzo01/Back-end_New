from getpass import getpass
login = input("Login tanlang: ")

if len(login) > 5:
    parol1 = getpass("Parol tanlang: ")
    if len(parol1) > 2:
        parol2 = getpass("Parolni qayta kiriting: ")
        if parol1 == parol2:
            print(
                "Siz tizimdan muvaffaqiyatli ro'yhatdan o'tdingiz :)\n"
                "Sizning logingiz: ", login)
        else:
            print("Parol xato terildi!")
    else:
        print("Parol kamida 8 ta belgidan iborat bo'shi kerak!")
else:
    print("Parol kamida 6 ta belgidan iborat bo'lishi kerak!")
input()