from re import fullmatch
while True:
    try:
        print('NO' if fullmatch('[^@.][^@]*(?<!\.)@(?!\.)[^@]*\.[^@]*[^@.]', input()) is None else 'YES')
    except EOFError:
        break

############## another solution ##############

while True:
    try:
        mystr = input()
        if mystr.count('@') == 1 and mystr[0] != '@' and mystr[0] != '.' and mystr[-1] != '@' and mystr[-1] != '.' and '@.' not in mystr and '.@' not in mystr:
            if '.' in mystr.split('@')[-1]:
                print('YES')
                continue
        print('NO')
    except EOFError:
        break
