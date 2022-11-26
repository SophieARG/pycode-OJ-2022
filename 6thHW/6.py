mydict1 = {}
mydict2 = {}
for i in range(int(input())):
    name, month, day = input().split()
    monthday = (int(month), int(day))
    if monthday in mydict1:
        mydict1[monthday].append(name)
    elif monthday in mydict2:
        mydict1[monthday] = [mydict2[monthday], name]
        del mydict2[monthday]
    else:
        mydict2[monthday] = name
if mydict1:
    for monthday in sorted(mydict1.keys()):
        mydict1[monthday].sort(key = lambda x: (len(x), x))
        print(*monthday, *mydict1[monthday])
        flag = False
else:
    print(None)
