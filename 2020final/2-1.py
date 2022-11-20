num = int(input())
res = 0
while True:
    num, mod = divmod(num, 2)
    if mod == 0:
        res += 1
    else:
        break
print(res)
    
