a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a-b)
print(a|b)
print(a.symmetric_difference(b))
a.symmetric_difference_update(b)
print(a)
for i in a:
    print(i)

