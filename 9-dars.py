# sozlar = ["bilaman", "pythonni", "Men"]
# print(sozlar[2] + " " + sozlar[1] + " +" +sozlar[0])

# l = ['y', 'n', 'o', 'h', 't', 'p'] # Python

# print(l[5] +l[0] + l[4])

# Listlar bilan ishlash!

mlist = [1, 2, 3, 88, 88, 88]
mlist2 = ["python", "delphi", "pascal"]
a = mlist + mlist2
print(a)
mlist3 = list(range(10, 20, 3))
print(mlist3)
for i in mlist2:
    print(i)
mlist.append(4)
mlist.insert(0, 4)
print(mlist)
mlist.pop()
mlist.pop(0)
mlist.remove(88)
print(len(mlist))
print(88 in mlist)
print(mlist.index(88))
print(mlist)

# Listlar bilan ishlash2!

# arr = [1, 2, 1, 5, 2, 1, 8, 3, 2]

# print(arr, count(1))
# print(arr, count(5))
# print(arr, count(55))

mlist = [1, 2, 3]
mlist2 = mlist.copy()  # 1-usul listdan nusxa olish
mlist2 = list(mlist)     # 2-usul listdan nusxa olish
mlist[1] = 5

print(mlist)
# print(mlist2)

# mylist = [1, 2, 3, 4]