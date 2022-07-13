mylist = [1, 3, 5, 6, 7, 8, 9, 10, 14, 16]
son = 14
low = 0
high = len(mylist) - 1
while high >= low:
    mid = (low + high) // 2
    if mylist[mid] == son:
        print("Topildi", son, mid)
        break
    elif mylist[mid] > son:
        high = mid
    else:
        low = mid
print("Finished")