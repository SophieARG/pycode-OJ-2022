a = int(input())
if a % 400 == 0:
    print('Y')
elif a % 100 == 0:
    print('N')
elif a % 4 == 0:
    print('Y')
else:
    print('N')
