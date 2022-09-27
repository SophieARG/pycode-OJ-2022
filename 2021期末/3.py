def isleap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def legalyear(year):
    date = str(year) + str(year)[::-1]
    m = int(date[-4: -2])
    d = int(date[-2:])
    if 1 <= m <= 12:
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= d <= 31:
                return date
        elif m in [4, 6, 9, 11]:
            if 1 <= d <= 30:
                return date
        else:
            if isleap(year):
                if 1 <= d <= 29:
                    return date
            else:
                if 1 <= d <= 28:
                    return date
    return False
    
date = input()
res = []
for i in range(1000, int(date[: 4]) + 1):
    legal = legalyear(i)
    if legal:
        res.append(legal)
if int(res[-1]) > int(date):
    res.pop()
print(' '.join(res))
