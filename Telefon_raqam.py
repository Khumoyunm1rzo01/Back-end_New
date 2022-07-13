tel = input("Telefon raqamingizni kiriting: ")
if len(tel) == 13:
    if tel[0] == "+":
        if tel[1:].isdigit():
            comp_code = tel[4:6]
            print(comp_code)
            if comp_code == "99" or comp_code == "95":
                print(tel[6:], "Ushbu raqam UzMobile kompaniyasiga tegishli!")
            elif comp_code == "90" or comp_code == "91":
                print(tel[6:], "Ushbu raqam Beeline kompaniyasiga tegishli!")
            elif comp_code == "93":
                print(tel[6:], "Ushbu raqam Ucell kompaniyasiga tegishli!")
            elif comp_code == "97" or comp_code == "88":
                print(tel[6:], "Ushbu raqam MobiUz kompaniyasiga tegishli!")
            elif comp_code == "33":
                print(tel[6:], "Ushbu raqam Humans kompaniyasiga tegishli!")
        else: 
            print("Raqamlar bo'lishi kerak!")
    else:
        print("+ dan boshlanishi kerak!")
else:
    print("Raqam xato!")
    
input()
