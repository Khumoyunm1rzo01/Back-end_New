matn = input("So'zni kiriting: ")
if len(matn) > 4:
    print(matn[:5])
else:
    print(matn + '-'*(5 - len(matn)))