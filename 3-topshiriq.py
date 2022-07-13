mylist = ["Hello", "Python.py", "C++.py", "Microsoft"]
mlist = ".py"
sozlar_topilsin = []
for word in mylist:
    if mlist in word:
        sozlar_topilsin.append(word)

print(sozlar_topilsin) 